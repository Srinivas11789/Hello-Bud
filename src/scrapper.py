# Download Modules : Requests (HTTP), Re (Regular Expression), Google-Search-API
from google import google
import requests
import re
import hashlib

def search(question):
   num_page = 3
   search_results = google.search(question, num_page)
   return search_results

def alexa_rank(url):
    request = 'http://data.alexa.com/data?cli=10&url=' + url
    try:
        page = requests.get(request)
        adata = page.text
    except requests.exceptions.RequestException as e:
        print e

    rank = re.search('POPULARITY.*TEXT="([0-9]+)"',adata.strip())
    if rank.group(1):
        return rank.group(1)
    else:
        print "Rank Not Found"

#Unit Test
#rank = alexa_rank("github.com/Hello-Bud")
#print rank
