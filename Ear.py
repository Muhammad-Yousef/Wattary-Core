# Wattary's Ear
# NOTE: this file requires PyAudio & Python Speech Recognition Engine because it uses the Microphone class

#Importing the nodule
import speech_recognition as sr

# obtain audio from the microphone
Ear = sr.Recognizer()
with sr.Microphone() as source:
    print("Listening!")
    audio = Ear.listen(source)

# recognize speech using Google Speech Recognition
try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")` instead of `r.recognize_google(audio)`
    text = Ear.recognize_google(audio)
    print(text)
except sr.UnknownValueError:
    print("I can't hear you, Could you repeat that please? ")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))