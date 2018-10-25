#!/usr/bin/python
'''
Created for site fetching purpose
on 25/10/18
'''

import requests

def url(url):

    r=requests.get(url)
    print("Get request output",url,"\n text content\n",r.text)
    text=r.text
    a=open("googl.com", "w")
    a.write(text)
    a.close()


url("https://www.google.com")

