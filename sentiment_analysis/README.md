# YouTube Video Sentiment Analysis

This project analyzes the sentiment of speech in YouTube videos using AssemblyAI's speech-to-text and sentiment analysis capabilities. It downloads the audio from YouTube videos, transcribes the speech, and performs sentiment analysis on the transcribed text.

[![GitHub](https://img.shields.io/badge/GitHub-Repository-blue)](https://github.com/Tamanna5/speech_recognition.git)

## Features

- Download audio from YouTube videos
- Transcribe speech to text using AssemblyAI
- Perform sentiment analysis on the transcribed text
- Save transcripts and sentiment analysis results
- Generate sentiment summaries with examples

## Prerequisites

- Python 3.8 or higher
- FFmpeg installed on your system
- AssemblyAI API key
- Internet connection

## Installation

1. Clone this repository:
```bash
git clone https://github.com/Tamanna5/speech_recognition.git
cd speech_recognition/sentiment_analysis
```

2. Install required Python packages:
```bash
pip install yt-dlp requests
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

4. Set up your AssemblyAI API key:
- Sign up at [AssemblyAI](https://www.assemblyai.com/)
- Get your API key from the dashboard
- Replace the API key in the notebook with your own

## Usage

1. Open the Jupyter notebook:
```bash
jupyter notebook main.ipynb
```

2. Run the cells in sequence to:
   - Set up the environment
   - Define helper functions
   - Process a YouTube video

3. When prompted, enter a YouTube video URL to analyze.

## Output

The script generates:
- A text file with the full transcript
- A JSON file with sentiment analysis results
- A summary of sentiments including:
  - Number of positive, negative, and neutral statements
  - Example positive and negative statements

## Project Structure

```
speech_recognition/
├── sentiment_analysis/      # This project
│   ├── main.ipynb          # Main Jupyter notebook
│   ├── README.md           # This file
│   ├── data/               # Generated data directory
│   │   ├── transcripts/    # Saved transcripts
│   │   └── sentiments/     # Sentiment analysis results
│   └── downloads/          # Downloaded audio files
```

## How It Works

1. **Audio Download**: Uses yt-dlp to download audio from YouTube videos
2. **Transcription**: Uploads audio to AssemblyAI for speech-to-text conversion
3. **Sentiment Analysis**: Analyzes the sentiment of each transcribed segment
4. **Results Processing**: Saves and summarizes the results

## Limitations

- Requires an active internet connection
- AssemblyAI API has usage limits based on your plan
- Processing time depends on video length and API response time

## Contributing

Feel free to submit issues and enhancement requests through the [GitHub repository](https://github.com/Tamanna5/speech_recognition.git)!

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Author

- [Tamanna](https://github.com/Tamanna5)
