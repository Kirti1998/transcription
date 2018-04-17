
import speech_recognition as sr
from os import path
import os.path


r = sr.Recognizer()
list_of_file = input("Enter the file name")
if os.path.exists(list_of_file):
    print("File found")
else:
    print("Error")
with sr.AudioFile(list_of_file) as source:
    audio = r.record(source)

print("Converting To Text...")
txt= r.recognize_sphinx(audio)

try:
    file =open('abc.txt','w')
    file.write(txt)
    file.close()
    print('saved')
except sr.UnknownValueError:
    print("Sphinx could not understand audio")
except sr.RequestError as e:
    print("Sphinx error; {0}".format(e))