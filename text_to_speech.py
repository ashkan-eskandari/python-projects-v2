import requests
import os
from elevenlabs import generate, play, Voice, VoiceSettings, generate, save
from elevenlabs import set_api_key

# ELEVEN_LABS_KEY = os.environ.get('ELEVEN_LABS_KEY')
set_api_key("c9e7b9cd10fb65d631c79b16c96d31f9")
def get_audio(text):
    audio = generate(
        text=text,
        output_format="mp3_44100_128",
        voice=Voice(
            voice_id='EXAVITQu4vr4xnSDxMaL',
            settings=VoiceSettings(stability=0.5, similarity_boost=0.5)))
    audio_file_path = "UPLOADS/audio/audio_path.mp3"
    save(
        audio,
        audio_file_path
    )
    return audio_file_path

# def get_audio():
# url = "https://api.elevenlabs.io/v1/text-to-speech/21m00Tcm4TlvDq8ikWAM"
# headers = {
#     "Accept": "audio/mpeg",
#     "Content-Type": "application/json",
#     "xi-api-key": ELEVEN_LABS_KEY
# }
#
# data = {
#     "text": text,
#     "model_id": "eleven_monolingual_v1",
#     "voice_settings": {
#         "stability": 0.5,
#         "similarity_boost": 0.5
#     }
# }
#
# response = requests.post(url, json=data, headers=headers)
# audio_content = response.content
# audio_file_path = "UPLOADS/audio/audio_path.mp3"
# with open(audio_file_path, "wb") as audio_file:
#     audio_file.write(audio_content)

# play(audio)
# return audio_file_path



