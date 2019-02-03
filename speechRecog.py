# import speech_recognition as sr
# dir(sr)
# for index, name in enumerate(sr.Microphone.list_microphone_names()):
#     print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))
# m = Microphone(device_index = 1)
import speech_recognition as sr

# get audio from the microphone
r = sr.Recognizer()
mic = sr.Microphone()

def loop():
    with mic as source:
        print("Speak:")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source, timeout=1)
        try:
            print("You said " + r.recognize_google(audio))
            # if(r.recognize_google(audio) == "left"):
            # 	print("Trying to turn left")
        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))

loop()
