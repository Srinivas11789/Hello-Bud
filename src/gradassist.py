# Download Modules : Requests (HTTP), Re (Regular Expression), Google-Search-API
import requests
import re
import json

def getcurriculum(course = ""):
    request = 'http://engineering.nyu.edu/academics/programs/computer-science-ms/curriculum/'
    try:
        page = requests.get(request)
        gdata = page.text
        return gdata
    except requests.exceptions.RequestException as e:
        print e


# Unit Test

#s = getcurriculum()
#print s
