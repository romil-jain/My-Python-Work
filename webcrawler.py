#Script for finding all the links in a web page
import urllib.request,urllib.parse,urllib.error
from bs4 import BeautifulSoup

url=input('Enter the URL of the page - ')
html=urllib.request.urlopen(url).read()
soup=BeautifulSoup(html,'html.parser')

tags=soup('a')
for tag in tags:
    print(tag.get('href',None))