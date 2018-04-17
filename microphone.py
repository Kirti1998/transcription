import split
import speech_recognition as sr

# use the audio file as the audio source
r = sr.Recognizer()
with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)
    print("listening...")
    audio = r.listen("E:/song/abc.wav")  # read the entire audio file


if __name__ == '__main__':
    split.main()
    IBM_USERNAME = "2b9202b6-b6c5-479e-9b2d-e193bd9eb2e2"  # IBM Speech to Text usernames are strings of the form XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX
    IBM_PASSWORD = "RXnrrDmLUg21"  # IBM Speech to Text passwords are mixed-case alphanumeric strings
    try:
        print("IBM Speech to Text thinks you said " + r.recognize_ibm(audio, username=IBM_USERNAME,
                                                                      password=IBM_PASSWORD))
    except sr.UnknownValueError:
        print("IBM Speech to Text could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from IBM Speech to Text service; {0}".format(e))
