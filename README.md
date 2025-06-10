# Speech Recognition Project

A comprehensive speech recognition project with multiple implementations, ranging from basic audio processing to advanced speech-to-text conversion and sentiment analysis.

[![GitHub](https://img.shields.io/badge/GitHub-Repository-blue)](https://github.com/Tamanna5/speech_recognition.git)

## Project Overview

This repository contains three distinct implementations of speech processing and recognition:

1. **Basic Implementation** (`/basic`)
   - Basic audio recording and processing
   - Waveform visualization
   - Audio format conversion
   - Perfect for learning fundamentals

2. **Simple Speech Recognition** (`/simple_speech_recognition`)
   - Speech-to-text conversion using AssemblyAI
   - Multiple language support
   - Multiple output formats
   - Speaker detection

3. **Sentiment Analysis** (`/sentiment_analysis`)
   - YouTube video audio analysis
   - Speech transcription
   - Sentiment analysis of transcribed text
   - Detailed sentiment summaries

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
├── sentiment_analysis/        # YouTube video sentiment analysis
│   ├── main.ipynb          # Jupyter notebook for analysis
│   ├── README.md           # Sentiment analysis documentation
│   ├── data/               # Generated data directory
│   └── downloads/          # Downloaded audio files
│
└── README.md               # This file
```

## Getting Started

Each implementation has its own README file with detailed setup and usage instructions. Choose the implementation that best suits your needs:

1. For learning basics: [Basic Implementation](basic/README.md)
2. For speech-to-text: [Simple Speech Recognition](simple_speech_recognition/README.md)
3. For sentiment analysis: [Sentiment Analysis](sentiment_analysis/README.md)

## Common Prerequisites

- Python 3.8 or higher
- FFmpeg (for audio processing)
- Internet connection (for API-based implementations)
- AssemblyAI API key (for advanced implementations)

## Installation

1. Clone this repository:
```bash
git clone https://github.com/Tamanna5/speech_recognition.git
cd speech_recognition
```

2. Install common dependencies:
```bash
pip install numpy matplotlib PyAudio wave requests yt-dlp
```

3. Install FFmpeg:
- On macOS:
```bash
brew install ffmpeg
```
- On Ubuntu/Debian:
```bash
sudo apt-get install ffmpeg
```
- On Windows:
Download from [FFmpeg website](https://ffmpeg.org/download.html)

## Learning Path

1. Start with the basic implementation to understand audio processing fundamentals
2. Move to simple speech recognition to learn about speech-to-text conversion
3. Explore sentiment analysis to understand how to analyze speech content

## Contributing

Feel free to contribute to any of the implementations:
1. Report bugs
2. Suggest improvements
3. Add new features
4. Improve documentation

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Author

- [Tamanna](https://github.com/Tamanna5)

## Acknowledgments

- [AssemblyAI](https://www.assemblyai.com/) for providing the speech-to-text API
- [PyAudio](https://people.csail.mit.edu/hubert/pyaudio/) for audio processing capabilities
- [yt-dlp](https://github.com/yt-dlp/yt-dlp) for YouTube audio downloading