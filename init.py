from os.path import join, dirname
from watson_developer_cloud import TextToSpeechV1
from watson_developer_cloud import SpeechToTextV1
import json
text_to_speech = TextToSpeechV1(
    username='dfdb445b-6a54-4bcd-a338-89f6a47b5251',
    password='ubqs8oKvTBY4',
    x_watson_learning_opt_out=False)  # Optional flag
speech_to_text=SpeechToTextV1()









print(json.dumps(text_to_speech.voices(), indent=2))

with open(join(dirname(__file__), 'output.wav'), 'wb') as audio_file:
       audio_file.write(text_to_speech.synthesize('Hello world!', accept='audio/wav', voice="en-US_AllisonVoice"))
with open(join(dirname(__file__), 'output.wav'),
                  'wb') as audio_file:    audio_file.write(text_to_speech.synthesize('Hello world!', accept='audio/wav',
                                           voice = "en-US_AllisonVoice"))

print(json.dumps(text_to_speech.pronunciation('Watson', pronunciation_format='spr'), indent=2))


print(json.dumps(text_to_speech.customizations(), indent=2))
