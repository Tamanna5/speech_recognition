# Simple Speech Recognition

A straightforward implementation of speech-to-text conversion using AssemblyAI's API.

## Features

- Audio file transcription
- Multiple language support
- Multiple output formats (TXT and JSON)
- Speaker detection
- Automatic punctuation
- Progress tracking

## Prerequisites

- Python 3.x
- AssemblyAI API key
- Required Python packages (install using `pip install -r requirements.txt`):
  - requests
  - assemblyai

## Setup

1. Create an `api_secrets.py` file in this directory with your AssemblyAI API key:
```python
API_KEY_ASSEMBLYAI = "your_api_key_here"
```

2. Install the required packages:
```bash
pip install -r requirements.txt
```

## Usage

Run the script:
```bash
python main.py
```

The script will:
1. Prompt you to enter the path to your audio file
2. Ask for your preferred output format (TXT, JSON, or both)
3. Let you select the language for transcription
4. Process the audio file and save the transcription

### Supported Languages

- English (en)
- Spanish (es)
- French (fr)
- German (de)
- Italian (it)

### Output Formats

1. Text File (.txt)
   - Contains the transcribed text with proper formatting
   - Includes speaker labels if multiple speakers are detected

2. JSON File (.json)
   - Contains detailed transcription data including:
     - Full text
     - Timestamps
     - Speaker labels
     - Confidence scores
     - Punctuation

## File Structure

```
simple_speech_recognition/
├── main.py           # Main script
├── api_02.py         # API interaction functions
├── api_secrets.py    # API key configuration
└── README.md         # This file
```

## Example

```bash
$ python main.py
Welcome to Audio Transcription!
--------------------------------
Enter the path to your audio file (e.g., audio.mp3): sample.mp3

Select output format:
1. Text file (.txt)
2. JSON file (.json)
3. Both formats
Enter your choice (1-3): 3

Select language:
1. English (en)
2. Spanish (es)
3. French (fr)
4. German (de)
5. Italian (it)
Enter your choice (1-5): 1

Processing file: sample.mp3
Uploading file to AssemblyAI...
Transcribing audio...
Progress: [====================] 100%

Transcription completed successfully!
Text transcript saved to: sample_20240321_123456.txt
JSON transcript saved to: sample_20240321_123456.json

Thank you for using Audio Transcription!
```

## Error Handling

The script includes comprehensive error handling for:
- Invalid file paths
- API errors
- Network issues
- Invalid user input

## Notes

- Maximum file size: 5MB
- Supported audio formats: MP3, WAV, M4A, etc.
- Processing time depends on audio length and server load
- API key should be kept secure and not shared

## Troubleshooting

If you encounter any issues:
1. Verify your API key is correct
2. Check your internet connection
3. Ensure the audio file is in a supported format
4. Verify the file size is within limits

## License

This implementation is part of the main Speech Recognition project and is licensed under the MIT License. 