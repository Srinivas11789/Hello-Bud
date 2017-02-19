#!/usr/bin/env python

from  AppKit import NSSpeechSynthesizer
import time
import sys
import speech_recognition

# Some Initialisation for Speech recognition and Speech synthesizer
mySpeechRecognizer = speech_recognition.Recognizer()
nssp = NSSpeechSynthesizer
myAssistant = nssp.alloc().init()

# Setting the voice to Victoria
myVoice = "com.apple.speech.synthesis.voice.Victoria"
myAssistant.setVoice_(myVoice)

## Listen voice function which will listen for voice input from the user
## No arguments as Mic is used as default source
## returns the Audio sample which is recorded from Mic
def listenVoice():
  with speech_recognition.Microphone() as source:
    mySpeechRecognizer.adjust_for_ambient_noise(source)
    myAudioInput = mySpeechRecognizer.listen(source)
  try:
    return mySpeechRecognizer.recognize_google(myAudioInput)
  except speech_recognition.UnknownValueError:
    print("Listening....")
  except speech_recognition.RequestError as e:
    print("Recog Error; {0}".format(e))
  return ""



## Speak voice function which speaks the given input
## One "String" Argument which is the text to speak
## returns nothing
def speakVoice(aPhrase):
  myAssistant.startSpeakingString_(aPhrase)
  while myAssistant.isSpeaking():
    time.sleep(2)



## Listen text function which takes text input from command line
## No arguments
## returns the specified input
def listenText():
  myInputText = raw_input('Wassup Buddy :')
  return myInputText




## Speak text function which will print the text given
## One argument which is to be printed
## returns nothing
def speakText(aText):
  print(aText)



#Unit test
speakVoice("Hello")
# myVoice = listenVoice()
