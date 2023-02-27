import speech_recognition as sr

# create a recognizer instance
r = sr.Recognizer()

# use the default microphone as the audio source
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)

# recognize speech using Google Speech Recognition
try:
    recognized_text = r.recognize_google(audio, language='auto')
    print("You said: " + recognized_text)

    # detect the language of the speech using Google Speech Recognition API
    language = r.recognize_google(audio, show_all=True)['language']
    print("Language detected: " + language)

except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))