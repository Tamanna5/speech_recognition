import matplotlib.pyplot as plt
import numpy as np
import wave

obj = wave.open("wav_file.wav", "rb")

sample_freq = obj.getframerate()
n_samples = obj.getnframes()
signal_wave = obj.readframes(-1)
obj.close()

t_audio = n_samples/sample_freq
print(t_audio)

signal_array = np.frombuffer(signal_wave, dtype=np.int16)
times = np.linspace(0., t_audio, num=len(signal_array))

plt.figure(figsize=(15,5))
plt.plot(times, signal_array)
plt.xlabel("Time [s]")
plt.ylabel("Signal Wave")
plt.title("Audio Signal")
plt.xlim(0, t_audio)
plt.show()
