import requests
import time
from api_secrets import API_KEY_ASSEMBLYAI


upload_endpoint = 'https://api.assemblyai.com/v2/upload'
transcript_endpoint = 'https://api.assemblyai.com/v2/transcript'

headers_auth_only = {
    "Authorization": API_KEY_ASSEMBLYAI
}

headers = {
    "authorization": API_KEY_ASSEMBLYAI,
    "content-type": "application/json"
}

CHUNK_SIZE = 5_242_880  # 5MB


def read_file(filename, chunk_size=5242880):
    with open(filename, 'rb') as f:
        while True:
            data = f.read(chunk_size)
            if not data:
                break
            yield data


def upload(filename):
    upload_response = requests.post(upload_endpoint, headers=headers_auth_only, data=read_file(filename))
    upload_response.raise_for_status()
    return upload_response.json()["upload_url"]


def transcribe(audio_url):
    transcript_request = {
        'audio_url': audio_url
    }

    transcript_response = requests.post(transcript_endpoint, json=transcript_request, headers=headers)
    return transcript_response.json()['id']

        
def poll(transcript_id):
    polling_endpoint = transcript_endpoint + '/' + transcript_id
    polling_response = requests.get(polling_endpoint, headers=headers)
    return polling_response.json()


def get_transcription_result_url(url):
    transcribe_id = transcribe(url)
    while True:
        data = poll(transcribe_id)
        if data['status'] == 'completed':
            return data, None
        elif data['status'] == 'error':
            return data, data['error']
            
        print("waiting for 30 seconds")
        time.sleep(30)
        
        
def save_transcript(audio_url, output_filename, language='en'):
    transcript_request = {
        "audio_url": audio_url,
        "language_code": language,
        "punctuate": True,
        "format_text": True,
        "speaker_labels": True
    }
    
    transcript_response = requests.post(transcript_endpoint, json=transcript_request, headers=headers_auth_only)
    transcript_response.raise_for_status()
    transcript_id = transcript_response.json()["id"]
    
    # Poll for transcription completion
    while True:
        polling_response = requests.get(f"{transcript_endpoint}/{transcript_id}", headers=headers_auth_only)
        polling_response.raise_for_status()
        transcript_data = polling_response.json()
        
        if transcript_data["status"] == "completed":
            return transcript_data
        elif transcript_data["status"] == "error":
            raise Exception(f"Transcription failed: {transcript_data.get('error', 'Unknown error')}")
        
        time.sleep(3)