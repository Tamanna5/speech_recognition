from api_02 import *
import os
import json
from datetime import datetime

def get_audio_file():
    while True:
        filename = input("Enter the path to your audio file (e.g., audio.mp3): ").strip()
        if not filename:
            print("Please enter a valid file path.")
            continue
            
        try:
            # Try to open the file to verify it exists
            with open(filename, 'rb') as f:
                return filename
        except FileNotFoundError:
            print(f"Error: File '{filename}' not found. Please enter a valid file path.")
        except Exception as e:
            print(f"Error: {str(e)}. Please try again.")

def get_output_format():
    print("\nSelect output format:")
    print("1. Text file (.txt)")
    print("2. JSON file (.json)")
    print("3. Both formats")
    while True:
        choice = input("Enter your choice (1-3): ").strip()
        if choice in ['1', '2', '3']:
            return choice
        print("Invalid choice. Please enter 1, 2, or 3.")

def get_language():
    print("\nSelect language:")
    print("1. English (en)")
    print("2. Spanish (es)")
    print("3. French (fr)")
    print("4. German (de)")
    print("5. Italian (it)")
    while True:
        choice = input("Enter your choice (1-5): ").strip()
        languages = {
            '1': 'en',
            '2': 'es',
            '3': 'fr',
            '4': 'de',
            '5': 'it'
        }
        if choice in languages:
            return languages[choice]
        print("Invalid choice. Please enter a number between 1 and 5.")

def save_output(transcript_data, output_format, base_filename):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    if output_format in ['1', '3']:  # Text file
        txt_filename = f"{base_filename}_{timestamp}.txt"
        with open(txt_filename, 'w', encoding='utf-8') as f:
            f.write(transcript_data['text'])
        print(f"\nText transcript saved to: {txt_filename}")
    
    if output_format in ['2', '3']:  # JSON file
        json_filename = f"{base_filename}_{timestamp}.json"
        with open(json_filename, 'w', encoding='utf-8') as f:
            json.dump(transcript_data, f, indent=2)
        print(f"JSON transcript saved to: {json_filename}")

def show_progress(current, total):
    bar_length = 50
    filled_length = int(round(bar_length * current / float(total)))
    percents = round(100.0 * current / float(total), 1)
    bar = '=' * filled_length + '-' * (bar_length - filled_length)
    print(f'\rProgress: [{bar}] {percents}%', end='')
    if current == total:
        print()

def main():
    print("Welcome to Audio Transcription!")
    print("--------------------------------")
    
    # Get audio file from user
    filename = get_audio_file()
    
    # Get output format preference
    output_format = get_output_format()
    
    # Get language preference
    language = get_language()
    
    print(f"\nProcessing file: {filename}")
    print("Uploading file to AssemblyAI...")
    
    try:
        # Upload the file and get the audio URL
        audio_url = upload(filename)
        
        # Save the transcript with progress indication
        print("\nTranscribing audio...")
        transcript_data = save_transcript(audio_url, 'transcript_output', language=language)
        
        # Save in selected format(s)
        base_filename = os.path.splitext(os.path.basename(filename))[0]
        save_output(transcript_data, output_format, base_filename)
        
        print("\nTranscription completed successfully!")
        
    except Exception as e:
        print(f"\nAn error occurred: {str(e)}")
    
    print("\nThank you for using Audio Transcription!")

if __name__ == "__main__":
    main()
