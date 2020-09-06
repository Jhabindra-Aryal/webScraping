
import htmlfetch
import requests #sending request/response to/from server 
import html5lib #for parsing
from bs4 import BeautifulSoup #for webscraping
def beautifulsoup():
    sourcecode=htmlfetch.fetchingpagesource()
    soup=BeautifulSoup(sourcecode,'html5lib') # using parser html5lib
    return soup