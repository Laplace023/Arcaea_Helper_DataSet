import requests
from bs4 import BeautifulSoup

# Making a GET request
r = requests.get('https://arcwiki.mcd.blue/Testify')

# check status code for response received
# success code - 200
print(r)

# Parsing the HTML
soup = BeautifulSoup(r.content, 'html.parser')

song = soup.find_all(class_="data")
print(song)
for s in song:
    print(s.text)
pst = soup.find_all(class_="pst-data")
for x in pst:
    print(x.text)

songByd = soup.find_all(class_="byd-label")
songEtr = soup.find_all(class_="etr-label")

print(len(songByd))
print(len(songEtr))