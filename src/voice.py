#!/usr/bin/env python

from  AppKit import NSSpeechSynthesizer
import time
import sys
import speech_recognition

recognizer = speech_recognition.Recognizer()

def listen():
  with speech_recognition.Microphone() as source:
                recognizer.adjust_for_ambient_noise(source)
                audio = recognizer.listen(source)
  try:
    print("You said " + recognizer.recognize_google(audio))
    #return recognizer.recognize_sphinx(audio)
    return recognizer.recognize_google(audio)
  except speech_recognition.UnknownValueError:
    print("Could not understand audio")
  except speech_recognition.RequestError as e:
    print("Recog Error; {0}".format(e))
  return ""


if len(sys.argv) < 2:
   text = raw_input('> ')
else:
   text = sys.argv[1]

nssp = NSSpeechSynthesizer

ve = nssp.alloc().init()

voices = ["com.apple.speech.synthesis.voice.Alex",
"com.apple.speech.synthesis.voice.Vicki",
"com.apple.speech.synthesis.voice.Victoria",
"com.apple.speech.synthesis.voice.Zarvox" ]

# for voice in nssp.availableVoices():
for voice in voices:
   ve.setVoice_(voice)
   print voice
   ve.startSpeakingString_(text)
   while ve.isSpeaking():
      time.sleep(1)

print("Speak now")
mystring = "You said" + listen()
for voice in voices:
   ve.setVoice_(voice)
   print voice
   ve.startSpeakingString_(mystring)
   while ve.isSpeaking():
      time.sleep(1)
print("Listening done")
#listen()
