import wave
obj = wave.open("wav_file.wav", "rb") #read in binary mode
print("Number of channels", obj.getnchannels())
print("Sample width", obj.getsampwidth())
print("Frame rate", obj.getframerate())
print("Number of frames", obj.getnframes())
print("parameters", obj.getparams())
#get the duration of the audio
t_audio = obj.getnframes() / obj.getframerate()
print(t_audio)

frames = obj.readframes(-1)
print(type(frames),type(frames[0]))
print(len(frames)/2)

obj.close()

obj.new = wave.open("new_wav_file.wav", "wb")
obj.new.setnchannels(obj.getnchannels())
obj.new.setsampwidth(obj.getsampwidth())
obj.new.setframerate(obj.getframerate())

obj.new.writeframes(frames)
obj.new.close()