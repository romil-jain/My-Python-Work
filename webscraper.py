#Python program to scrape website and save tutorials from website
#Uses third party python library - requests
import requests
from bs4 import BeautifulSoup
import csv
 
URL = "https://www.w3schools.com"
r = requests.get(URL)
 
soup = BeautifulSoup(r.content, 'html5lib')
 
tutorials=[]  # a list to store quotes
 
table = soup.find('div', attrs = {'class':'w3-bar-block'})
 
for row in table.findAll('a', attrs = {'class':'w3-bar-item w3-button'}):
    tutorial = {}
    tutorial['name'] = row.text
    tutorial['url'] = URL+row["href"]
    tutorials.append(tutorial)
 
filename = 'Online Web Tutorials.txt'
with open(filename, 'w') as f:
    f.write("TUTORIAL NAME"+"\t\t\t\t"+"URL\n")
    for tutorial in tutorials:
        f.write(tutorial["name"]+"\t\t\t\t"+tutorial["url"])
        f.write("\n")
f.close()