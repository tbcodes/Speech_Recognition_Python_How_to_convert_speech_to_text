# Truzz Blogg - Youtube link: https://www.youtube.com/watch?v=KcjHfnCteZg
# Speech recognition in Python ::: How to convert Speech to Text

import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print("Say Something...")
    audio = r.listen(source)

    try:
        text = r.recognize_google(audio, language='pt-BR')
        print("What did you say: {}".format(text))
    except:
        print("I am sorry! I can not understand!")