import wave
import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft
import sys
import os

def visualize_audio(filename):
    """
    Visualize audio file waveform and frequency spectrum.
    
    Args:
        filename (str): Path to the WAV file
    """
    if not os.path.exists(filename):
        print(f"Error: File '{filename}' not found.")
        return
    
    try:
        # Open the WAV file
        wf = wave.open(filename, 'rb')
        
        # Read audio data
        signal = np.frombuffer(wf.readframes(wf.getnframes()), dtype=np.int16)
        
        # Create time axis
        time = np.linspace(0, len(signal)/wf.getframerate(), len(signal))
        
        # Create frequency axis
        n = len(signal)
        freq = np.fft.fftfreq(n, 1/wf.getframerate())
        spectrum = np.abs(fft(signal))
        
        # Create figure with two subplots
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8))
        
        # Plot waveform
        ax1.plot(time, signal)
        ax1.set_title('Waveform')
        ax1.set_xlabel('Time (s)')
        ax1.set_ylabel('Amplitude')
        ax1.grid(True)
        
        # Plot frequency spectrum
        ax2.plot(freq[:n//2], spectrum[:n//2])
        ax2.set_title('Frequency Spectrum')
        ax2.set_xlabel('Frequency (Hz)')
        ax2.set_ylabel('Magnitude')
        ax2.grid(True)
        
        # Adjust layout and show plot
        plt.tight_layout()
        plt.show()
        
        # Print audio information
        print(f"\nAudio Information:")
        print(f"Channels: {wf.getnchannels()}")
        print(f"Sample width: {wf.getsampwidth()} bytes")
        print(f"Frame rate: {wf.getframerate()} Hz")
        print(f"Number of frames: {wf.getnframes()}")
        print(f"Duration: {wf.getnframes() / wf.getframerate():.1f} seconds")
        
        wf.close()
        
    except Exception as e:
        print(f"Error visualizing audio: {str(e)}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python visualize_audio.py <audio_file.wav>")
        sys.exit(1)
    
    visualize_audio(sys.argv[1]) 