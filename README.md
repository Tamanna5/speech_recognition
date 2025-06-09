 # Speech Recognition Project

A comprehensive speech recognition project with multiple implementations, ranging from basic audio processing to advanced speech-to-text conversion.

## Project Structure

```
speech_recognition/
├── basic/                    # Basic audio processing implementation
│   ├── record_audio.py      # Audio recording script
│   ├── play_audio.py        # Audio playback script
│   ├── visualize_audio.py   # Audio visualization script
│   └── README.md           # Basic implementation documentation
│
├── simple_speech_recognition/  # Advanced speech-to-text implementation
│   ├── main.py             # Main transcription script
│   ├── api_02.py           # API interaction functions
│   ├── api_secrets.py      # API key configuration
│   └── README.md           # Advanced implementation documentation
│
└── README.md               # This file
```

## Features

### Basic Implementation
- Audio recording from microphone
- Audio file playback
- Waveform visualization
- Frequency spectrum analysis
- Basic audio format conversion

### Advanced Implementation
- Audio file transcription using AssemblyAI
- Multiple language support
- Multiple output formats (TXT and JSON)
- Speaker detection
- Automatic punctuation
- Progress tracking

## Prerequisites

- Python 3.x
- Required Python packages:
  - numpy
  - matplotlib
  - PyAudio
  - wave
  - scipy
  - requests
  - assemblyai

## Installation

1. Install the required packages:
```bash
pip install numpy matplotlib PyAudio wave scipy requests assemblyai
```

2. For macOS users, install portaudio:
```bash
brew install portaudio
```

3. For the advanced implementation, create an `api_secrets.py` file in the `simple_speech_recognition` directory:
```python
API_KEY_ASSEMBLYAI = "your_api_key_here"
```

## Getting Started

### Basic Implementation

1. Record audio:
```bash
cd basic
python record_audio.py
```

2. Play recorded audio:
```bash
python play_audio.py recording_20240321_123456.wav
```

3. Visualize audio:
```bash
python visualize_audio.py recording_20240321_123456.wav
```

### Advanced Implementation

1. Navigate to the advanced implementation:
```bash
cd simple_speech_recognition
```

2. Run the transcription script:
```bash
python main.py
```

3. Follow the prompts to:
   - Select your audio file
   - Choose output format
   - Select language
   - Process the transcription

## Supported Languages (Advanced Implementation)

- English (en)
- Spanish (es)
- French (fr)
- German (de)
- Italian (it)

## Output Formats (Advanced Implementation)

1. Text File (.txt)
   - Transcribed text with proper formatting
   - Speaker labels for multiple speakers

2. JSON File (.json)
   - Detailed transcription data
   - Timestamps
   - Speaker labels
   - Confidence scores
   - Punctuation

## Technical Details

### Audio Parameters (Basic Implementation)
- Sample Rate: 44100 Hz
- Channels: 1 (Mono)
- Bit Depth: 16-bit
- Format: WAV

### Limitations (Advanced Implementation)
- Maximum file size: 5MB
- Supported formats: MP3, WAV, M4A
- Processing time varies with audio length

## Learning Resources

1. [Python Audio Processing](https://realpython.com/python-audio-processing/)
2. [PyAudio Documentation](https://people.csail.mit.edu/hubert/pyaudio/)
3. [AssemblyAI Documentation](https://www.assemblyai.com/docs)
4. [NumPy Documentation](https://numpy.org/doc/stable/)
5. [Matplotlib Documentation](https://matplotlib.org/stable/contents.html)

## Troubleshooting

### Basic Implementation
- Ensure microphone is properly connected
- Check audio device settings
- Verify file permissions

### Advanced Implementation
- Verify API key is correct
- Check internet connection
- Ensure audio file format is supported
- Verify file size is within limits

## Contributing

Feel free to:
1. Report bugs
2. Suggest improvements
3. Add new features
4. Improve documentation

## License

This project is licensed under the MIT License.