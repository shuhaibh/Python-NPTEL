#Program to take an audio file and convert it into text

import speech_recognition as sr
Audio_File=("Sample.wav")
#using audio file as source

r= sr.Recognizer()

with sr.AudioFile(Audio_File) as source:
    audio=r.record(source)
#reads the audio file

try:
    print("audio file contains "+r.recognize_google(audio))
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand your audio")
except sr.RequestError:
    print("couldn't get the result from Google Speech Recognition")
