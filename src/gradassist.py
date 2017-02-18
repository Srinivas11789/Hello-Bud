# Download Modules : Requests (HTTP), Re (Regular Expression), Google-Search-API
import requests
import re
import json

with open('profile.json') as data_file:
    data = json.load(data_file)


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
        for course in courses:
            if str(course['time']).lower()[0:3]==str(time).lower():
                return course
            else:
                continue
        return None


def getEvents(type='default'):
    events = data['events']
    if type=='default':
        return events

    else:
        eventsList = []
        for event in events:
            if str(event['type']).lower() == str(type).lower():
                eventsList.append(event)
        return eventsList




print getEvents(type="hackathon")
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