import speech_recognition as sr

def getInput():
    # obtain audio from the microphone
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)

    # recognize speech using GSR
    try:
        command = r.recognize_google(audio, language='en-in')
        print(f"User said: {command}\n")
        return command
    except sr.UnknownValueError:
        print("RENO could not understand audio")
        return "None"
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
        return "None"