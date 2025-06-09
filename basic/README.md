# Basic Speech Recognition

A simple implementation of speech recognition using Python's built-in libraries and basic audio processing techniques.

## Overview

This implementation provides a foundation for speech recognition using basic audio processing techniques. It's designed to be educational and help understand the fundamentals of speech recognition before moving to more advanced implementations.

## Features

- Basic audio recording functionality
- Simple audio file processing
- Waveform visualization
- Basic audio format conversion
- Audio playback capabilities

## Prerequisites

- Python 3.x
- Required Python packages:
  - numpy
  - matplotlib
  - PyAudio
  - wave

## Installation

1. Install the required packages:
```bash
pip install numpy matplotlib PyAudio wave
```

2. For macOS users, you might need to install portaudio first:
```bash
brew install portaudio
```

## Usage

### Recording Audio
```python
python record_audio.py
```
This will:
- Start recording audio from your microphone
- Save it as a WAV file
- Display the waveform

### Playing Audio
```python
python play_audio.py your_audio_file.wav
```
This will:
- Load the specified audio file
- Play it through your speakers
- Display basic audio information

### Visualizing Audio
```python
python visualize_audio.py your_audio_file.wav
```
This will:
- Load the audio file
- Display its waveform
- Show frequency spectrum

## File Structure

```
basic/
├── record_audio.py      # Audio recording script
├── play_audio.py        # Audio playback script
├── visualize_audio.py   # Audio visualization script
└── README.md           # This file
```

## Example

```python
# Recording audio
$ python record_audio.py
Recording... Press Ctrl+C to stop
Recording saved as: recording_20240321_123456.wav

# Playing audio
$ python play_audio.py recording_20240321_123456.wav
Playing audio file...
Duration: 5.2 seconds
Sample rate: 44100 Hz
Channels: 1

# Visualizing audio
$ python visualize_audio.py recording_20240321_123456.wav
Generating waveform visualization...
```

## Technical Details

### Audio Parameters
- Sample Rate: 44100 Hz
- Channels: 1 (Mono)
- Bit Depth: 16-bit
- Format: WAV

### Features
1. **Audio Recording**
   - Real-time microphone input
   - Automatic file naming with timestamps
   - Configurable recording duration

2. **Audio Playback**
   - Support for WAV files
   - Basic audio information display
   - Error handling for invalid files

3. **Visualization**
   - Waveform display
   - Time-domain representation
   - Basic frequency analysis

## Limitations

- Basic implementation without advanced features
- Limited to WAV format
- No noise reduction
- No speech recognition capabilities
- Basic error handling

## Learning Resources

1. [Python Audio Processing](https://realpython.com/python-audio-processing/)
2. [PyAudio Documentation](https://people.csail.mit.edu/hubert/pyaudio/)
3. [NumPy Documentation](https://numpy.org/doc/stable/)
4. [Matplotlib Documentation](https://matplotlib.org/stable/contents.html)

## Next Steps

After understanding the basics, you can:
1. Move to the `simple_speech_recognition` implementation
2. Add noise reduction
3. Implement basic speech detection
4. Add more audio formats support

## Contributing

Feel free to:
1. Report bugs
2. Suggest improvements
3. Add new features
4. Improve documentation

## License

This implementation is part of the main Speech Recognition project and is licensed under the MIT License. 