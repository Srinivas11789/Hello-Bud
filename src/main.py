# Project: Hello! Bud @ HackNyu
# Main.py

# Module Import
import animation	# To Perform the Assistant Animation - In Progress
import scrapper      	# Scrapping the Web for Nest Results - In Progress
import gradassist  	# Graduate Assistant
import voice		# Voice recognition features



def startupFunction():
  myStartupText = "Hello! I am Alia"
  voice.speakVoice(myStartupText)


def waitForInput():
  while(1):
    inputText = str.lower(str(voice.listenVoice()))
    if inputText != "":
      print("input : " + inputText)
      if inputText.startswith('a') and (inputText.endswith('a') or inputText.endswith('h')):
        voice.speakVoice("Yes")
        inputQuery = voice.listenVoice()
        if inputQuery != "":
          print("Query :" + inputQuery)
          searchResult = scrapper.search(str(inputQuery))
          print(searchResult)

      
startupFunction()
waitForInput()
