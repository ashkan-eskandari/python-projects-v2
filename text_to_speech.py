import requests


key = "c9e7b9cd10fb65d631c79b16c96d31f9"


def get_audio(text):

    url = "https://api.elevenlabs.io/v1/text-to-speech/21m00Tcm4TlvDq8ikWAM"
    headers = {
        "Accept": "audio/mpeg",
        "Content-Type": "application/json",
        "xi-api-key": key
    }

    data = {
        "text": text,
        "model_id": "eleven_monolingual_v1",
        "voice_settings": {
            "stability": 0.5,
            "similarity_boost": 0.5
        }
    }

    response = requests.post(url, json=data, headers=headers)
    audio_content = response.content
    audio_file_path = "UPLOADS/audio/audio_path.mp3"
    with open(audio_file_path, "wb") as audio_file:
        audio_file.write(audio_content)
    return audio_file_path
