# Project: Hello! Bud @ HackNyu
# Main.py

# Module Import
#import animation	# To Perform the Assistant Animation - In Progress
import scrapper      	# Scrapping the Web for Nest Results - In Progress
import gradassist  	# Graduate Assistant
import voice		# Voice recognition features
import time


def startupFunction():
  myStartupText = "Hello! I am Alia"
  voice.speakVoice(myStartupText)


def waitForInput():
  while(1):
    inputText = str.lower(str(voice.listenVoice()))
    if inputText != "":
      print("input : " + inputText)
      #if inputText == "google":
      if inputText.startswith('a') and (inputText.endswith('a') or inputText.endswith('h')):
        voice.speakVoice("Yes")
        inputQuery = voice.listenVoice()
        if inputQuery != "":
          myString = str(inputQuery)
          if 'how' in myString:
            print("Query :" + inputQuery)
            searchResult = scrapper.search(myString)
            desc = searchResult[0].description
            print(desc)
            voice.speakVoice(desc)
            #myRank = scrapper.alexa_rank(searchResult[1].link)
            #print(myRank)
          elif 'deadline' in myString:
            myDeadlines = gradassist.getDeadlines()
            #code for telling ur deadlines
            for aDeadline in myDeadlines:
              for k,v in aDeadline.items():
                voice.speakVoice(str(k)+ str(v))
                time.sleep(5)
                #voice.speakVoice(str(v))
          elif 'schedule' in myString:
            mySchedule = gradassist.getCourse()
            #code for telling ur schedule
            for aSchedule in mySchedule:
              for k,v in aSchedule.items():
                voice.speakVoice(str(k)+ str(v))
                time.sleep(5)
                #voice.speakVoice(str(v))
          elif 'events' in myString:
            myEvents = gradassist.getEvents()
            #code for telling ur events
            for anEvent in myEvents:
              for k,v in anEvent.items():
                voice.speakVoice(str(k)+ str(v))
                time.sleep(5)
                #voice.speakVoice(str(v))
          elif 'first' in myString:
            myItems = gradassist.getDeadlines()
            smallest = 50
            targetItem = {}
            for aDeadline in myItems:
              remainingDays = aDeadline['days']
              if remainingDays < smallest:
                smallest = remainingDays
                targetItem = aDeadline
            textOutput = "You should consider finishing" + targetItem['subject'] + "because its due on" + targetItem['time'] + "and it will take" + targetItem['time_required']
            voice.speakVoice(textOutput)
            time.sleep(5)
          elif 'hard' in myString:
            myItems = gradassist.getCourse()
            difficulty = 0
            targetItem = {}
            for aCourse in myItems:
              myDifficulty = aCourse['difficulty']
              if myDifficulty > difficulty:
                difficulty = myDifficulty
                targetItem = aCourse
            textOutput = "You should concentrate more on" + targetItem['name'] + "as it is difficult than other courses"
            voice.speakVoice(textOutput)
            time.sleep(5)
          else:
            myDefaultString = "Am not sure about it. Sorry!"
            voice.speakVoice(myDefaultString) 

      
startupFunction()
waitForInput()
