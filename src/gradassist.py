# Download Modules : Requests (HTTP), Re (Regular Expression), Google-Search-API
import requests
import re
import json

def getcurriculum(course = ""):
    request = 'http://engineering.nyu.edu/academics/programs/computer-science-ms/curriculum/'
    gdata = request.text
    if course:
        
    try:
        page = requests.get(request)
        gdata = page.text
    except requests.exceptions.RequestException as e:
        print e


# Unit Test

#getcurriculum(course)
