import pyaudio
import websockets
import asyncio
import base64
import json
import os
import openai
import signal

# ========== API KEYS ==========
API_KEY_ASSEMBLYAI = os.getenv("ASSEMBLYAI_API_KEY", "YOUR_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "YOUR_API_KEY")

# Configure OpenAI client
openai.api_key = OPENAI_API_KEY

# ========== AUDIO CONFIG ==========
FRAMES_PER_BUFFER = 3200
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000

# Initialize PyAudio
p = pyaudio.PyAudio()

# AssemblyAI WebSocket URL
URL = f"wss://api.assemblyai.com/v2/realtime/ws?sample_rate={RATE}"

# Global control flag
running = True


def signal_handler(sig, frame):
    """Gracefully shut down"""
    global running
    print("\nExiting gracefully...")
    running = False


# Register signal handler
signal.signal(signal.SIGINT, signal_handler)


def ask_computer(prompt):
    """Get response from OpenAI"""
    try:
        completion = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are a helpful voice assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        return completion["choices"][0]["message"]["content"].strip()
    except Exception as e:
        return f"[OpenAI Error] {str(e)}"


async def send_receive():
    """Real-time audio streaming with AssemblyAI and OpenAI"""
    global running
    print(f'Connecting websocket to url {URL}')

    # Start microphone stream
    stream = p.open(
        format=FORMAT,
        channels=CHANNELS,
        rate=RATE,
        input=True,
        frames_per_buffer=FRAMES_PER_BUFFER
    )

    try:
        async with websockets.connect(
            URL,
            extra_headers=(("Authorization", API_KEY_ASSEMBLYAI),),
            ping_interval=5,
            ping_timeout=20
        ) as _ws:
            await asyncio.sleep(0.1)
            print("Receiving SessionBegins ...")
            session_begins = await _ws.recv()
            print(session_begins)

            response_data = json.loads(session_begins)
            if "error" in response_data:
                print(f"\n⚠️ AssemblyAI Error: {response_data['error']}")
                print("Note: Real-time transcription requires a paid AssemblyAI account.")
                return

            print("Listening and Responding... (Press Ctrl+C to stop)")

            async def send():
                """Send microphone audio to WebSocket"""
                while running:
                    try:
                        data = stream.read(FRAMES_PER_BUFFER, exception_on_overflow=False)
                        encoded = base64.b64encode(data).decode("utf-8")
                        await _ws.send(json.dumps({"audio_data": encoded}))
                        await asyncio.sleep(0.01)
                    except Exception as e:
                        print(f"[Send Error] {e}")
                        break

            async def receive():
                """Receive transcription and get OpenAI response"""
                while running:
                    try:
                        result_str = await _ws.recv()
                        result = json.loads(result_str)
                        prompt = result.get("text", "")
                        if prompt and result.get("message_type") == "FinalTranscript":
                            print("\nMe:", prompt)
                            answer = ask_computer(prompt)
                            print("Bot:", answer)
                            print("\n(Listening...)")
                    except Exception as e:
                        print(f"[Receive Error] {e}")
                        break

            send_task = asyncio.create_task(send())
            receive_task = asyncio.create_task(receive())

            done, pending = await asyncio.wait(
                [send_task, receive_task],
                return_when=asyncio.FIRST_COMPLETED
            )

            for task in pending:
                task.cancel()

    except Exception as e:
        print(f"[WebSocket Error] {e}")
    finally:
        stream.stop_stream()
        stream.close()


def main():
    """Entry point"""
    print("Voice Assistant Starting...")
    print("Speak clearly into your microphone.")
    print("Press Ctrl+C to exit.")

    try:
        asyncio.run(send_receive())
    except KeyboardInterrupt:
        print("\nTerminated by user.")
    finally:
        p.terminate()
        print("Resources cleaned up. Goodbye!")


if __name__ == "__main__":
    main()
