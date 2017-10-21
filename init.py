from os.path import join, dirname
from watson_developer_cloud import TextToSpeechV1
from watson_developer_cloud import SpeechToTextV1
import json
def TTS():
    text_to_speech = TextToSpeechV1(
    username='dfdb445b-6a54-4bcd-a338-89f6a47b5251',
    password='ubqs8oKvTBY4',
    x_watson_learning_opt_out=False)  # Optional flag
    print(json.dumps(text_to_speech.voices(), indent=2))
    with open(join(dirname(__file__), 'output.wav'), 'wb') as audio_file:
       audio_file.write(text_to_speech.synthesize('Hello world!', accept='audio/wav', voice="en-US_AllisonVoice"))
    with open(join(dirname(__file__), 'output.wav'),
                  'wb') as audio_file:    audio_file.write(text_to_speech.synthesize('Hello world!', accept='audio/wav',
                                           voice = "en-US_AllisonVoice"))
    print(json.dumps(text_to_speech.pronunciation('Watson', pronunciation_format='spr'), indent=2))
    print(json.dumps(text_to_speech.customizations(), indent=2))
def STT():

    speech_to_text = SpeechToTextV1(
    username='YOUR SERVICE USERNAME',
    password='YOUR SERVICE PASSWORD',
    )

print(json.dumps(speech_to_text.get_model('en-US_BroadbandModel'), indent=2))

     -
with open(join(dirname(__file__), '../resources/speech.wav'), 'rb') as audio_file:
    +
with open(join(dirname(__file__), '../resources/speech.wav'),
          +          'rb') as audio_file:
    print(json.dumps(speech_to_text.recognize(
        -        audio_file, content_type='audio/wav', timestamps=True, word_confidence=True), indent=2))
         + audio_file, content_type='audio/wav', timestamps = True,
                                                              +        word_confidence = True),
+        indent = 2))
