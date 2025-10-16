import speech_recognition as sr
AUDIO_FILE=("d:/Rgukt/Desktop/python/week5/rama_song.wav")
#use audio file as source
r=sr.Recognizer() # intialise the recogniser
with sr.AudioFile(AUDIO_FILE) as source:
    audio=r.record(source) #reads the audio file
try:
    print("audio file contains " + r.recognize_google(audio))
except sr.UnknownValueError :                                # exception is a type of error
    print("Google speech recognition could not understand audio")
except sr.RequestError :
    print("couldn't get the results from google speech Recognition")  