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
for s in song:
    print(s.text)
pst = soup.find_all(class_="pst-data")
for x in pst:
    print(x.text)