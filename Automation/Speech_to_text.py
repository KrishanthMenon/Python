import speech_recognition as sr
import pocketsphinx
r = sr.Recognizer()


try:
    with sr.Microphone() as source:                # use the default microphone as the audio source
        print("Listening...")
        audio = r.listen(source)                   # listen for the first phrase and extract it into audio data
        print("You said " + r.recognize_sphinx(audio))    # recognize speech using Google Speech Recognition
except LookupError:                                # speech is unintelligible
        print("Could not understand audio")