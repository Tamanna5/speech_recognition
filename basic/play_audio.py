import wave
import pyaudio
import sys
import os

def play_audio(filename):
    """
    Play a WAV audio file.
    
    Args:
        filename (str): Path to the WAV file
    """
    if not os.path.exists(filename):
        print(f"Error: File '{filename}' not found.")
        return
    
    try:
        # Open the WAV file
        wf = wave.open(filename, 'rb')
        
        # Print audio information
        print(f"\nAudio Information:")
        print(f"Channels: {wf.getnchannels()}")
        print(f"Sample width: {wf.getsampwidth()} bytes")
        print(f"Frame rate: {wf.getframerate()} Hz")
        print(f"Number of frames: {wf.getnframes()}")
        print(f"Duration: {wf.getnframes() / wf.getframerate():.1f} seconds")
        
        # Initialize PyAudio
        p = pyaudio.PyAudio()
        
        # Open stream
        stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                       channels=wf.getnchannels(),
                       rate=wf.getframerate(),
                       output=True)
        
        # Read data
        data = wf.readframes(1024)
        
        print("\nPlaying audio...")
        
        # Play stream
        while data:
            stream.write(data)
            data = wf.readframes(1024)
        
        # Cleanup
        stream.stop_stream()
        stream.close()
        p.terminate()
        wf.close()
        
        print("Playback completed.")
        
    except Exception as e:
        print(f"Error playing audio: {str(e)}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python play_audio.py <audio_file.wav>")
        sys.exit(1)
    
    play_audio(sys.argv[1])