import pyaudio
import wave
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
import time

def record_audio(filename=None, duration=None):
    """
    Record audio from microphone and save to WAV file.
    
    Args:
        filename (str): Output filename. If None, generates timestamp-based name
        duration (float): Recording duration in seconds. If None, records until Ctrl+C
    """
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100
    
    p = pyaudio.PyAudio()
    
    # Generate filename if not provided
    if filename is None:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"recording_{timestamp}.wav"
    
    print(f"Recording will be saved as: {filename}")
    print("Recording... Press Ctrl+C to stop")
    
    stream = p.open(format=FORMAT,
                   channels=CHANNELS,
                   rate=RATE,
                   input=True,
                   frames_per_buffer=CHUNK)
    
    frames = []
    start_time = time.time()
    
    try:
        while True:
            if duration and (time.time() - start_time) > duration:
                break
                
            data = stream.read(CHUNK)
            frames.append(data)
            
    except KeyboardInterrupt:
        print("\nRecording stopped by user")
    finally:
        stream.stop_stream()
        stream.close()
        p.terminate()
        
        # Save the recorded audio
        wf = wave.open(filename, 'wb')
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))
        wf.close()
        
        print(f"Recording saved as: {filename}")
        
        # Plot the waveform
        plot_waveform(filename)

def plot_waveform(filename):
    """
    Plot the waveform of the recorded audio.
    
    Args:
        filename (str): Path to the WAV file
    """
    # Read the WAV file
    wf = wave.open(filename, 'rb')
    signal = np.frombuffer(wf.readframes(wf.getnframes()), dtype=np.int16)
    
    # Create time axis
    time = np.linspace(0, len(signal)/wf.getframerate(), len(signal))
    
    # Plot
    plt.figure(figsize=(12, 4))
    plt.plot(time, signal)
    plt.title('Waveform')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    record_audio()