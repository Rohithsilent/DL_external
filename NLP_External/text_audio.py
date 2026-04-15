import speech_recognition as sr
import pyttsx3

recognizer = sr.Recognizer()
engine = pyttsx3.init()

with sr.AudioFile("input.wav") as source:
    print("listening")
    audio = recognizer.record(source)


try:
    text = recognizer.recognize_google(audio)
    print("converted text:",text)
except:
    print("could not understand")
    text =""


if text:
    print("converting text to audio")
    engine.save_to_file(text,"output.mp3")
    engine.runAndWait()

print("done")