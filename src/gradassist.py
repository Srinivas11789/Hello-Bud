# Download Modules : Requests (HTTP), Re (Regular Expression), Google-Search-API
import requests
import re
import json
import time
from time import mktime
from datetime import datetime

with open('profile.json') as data_file:
    data = json.load(data_file)

time_format = "%a, %d %b %Y %H:%M:%S %Z"


def getcurriculum(course = ""):
    request = 'http://engineering.nyu.edu/academics/programs/computer-science-ms/curriculum/'
    try:
        page = requests.get(request)
        gdata = page.text
        return gdata
    except requests.exceptions.RequestException as e:
        print e


def getDeadlines(type='default'):
    deadLines = data["deadlines"]
    if(type=='default'):
        return deadLines;
    else:
        assignments = []
        for deadLine in deadLines:
            if(str(deadLine["type"]).lower()==str(type).lower()):
                assignments.append(deadLine)
        return assignments


def getCourse(name='default', professor='default', time='default'):
    courses = data['courses']
    if name=='default'and professor=='default' and time=='default':
        return courses
    if name!='default':
        for course in courses:
            if(str(course['name']).lower()==str(name).lower()):
                return course
            else:
                continue
        return None
    elif professor!='default':
        for course in courses:
            if str(course['professor']).lower()==str(professor).lower():
                return course
            else:
                continue
        return None

    elif time!='default':
        courseList = []
        for course in courses:
            if str(course['time']).lower()[0:3]==str(time).lower():
                courseList.append(course)
            else:
                continue
        return courseList


def getEvents(type='default', subject='default', time='default'):
    events = data['events']
    eventsList = []
    if type=='default' and subject=='default' and time=='default':
        return events

    elif type!='default':
        for event in events:
            if str(event['type']).lower() == str(type).lower():
                eventsList.append(event)

    elif subject!='default':
        for event in events:
            if str(event['subject']).lower() == str(subject).lower():
                eventsList.append(event)

    elif time!='default':
        for event in events:
            if str(event['time']).lower()[0:3] == str(time).lower():
                eventsList.append(event)

    return eventsList

def timeDifference(t1,t2):
    t1 = time.struct_time(t1)
    t2 = time.struct_time(t2)
    dt1 = datetime.fromtimestamp(mktime(t1))
    dt2 = datetime.fromtimestamp(mktime(t2))

    return dt2 - dt1


#Suggetions


#events = getEvents(type='free food')
#t = time.strptime(events[0]['time'],time_format)
#print timeDifference(time.localtime(), t)

def deadLinePlanner(type='default'):

    currentTime = time.localtime()
    deadLines = getDeadlines(type=type)
    print deadLines

    sorted_deadlines = sorted(deadLines, key=lambda k:time.strptime(k['time'],time_format))
    return sorted_deadlines


print deadLinePlanner()

print getEvents(subject="machine learning")
# Unit Test
#course = getCourse(name="name_of_course)
#course = getCourse(professor="professor_handling_course")
#course = getCourse(time="Weekday")
#print course

#deadlines = getDeadlines(type='type_of_deadline')
#type_of_deadline : assignment, lab report etc.,
#Without any arguments, return all the deadlines

#events = getEvents(type='event_type')
#event types : hackathon, free food, seminar


#s = getcurriculum()
#print s