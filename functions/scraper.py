import requests
from bs4 import BeautifulSoup

# Making a GET request
r = requests.get('https://arcaea.fandom.com/wiki/TRPNO')

# check status code for response received
# success code - 200
print(r)

# Parsing the HTML
soup = BeautifulSoup(r.content, 'html.parser')

pst = soup.find_all("span", class_= 'pst')
for i in pst:
    print(i.text)
prs = soup.find_all(class_= 'prs')
print(prs)
ftr = soup.find_all(class_= 'ftr')
print(ftr)
bpm = soup.find_all(class_="pi-horizontal-group-item pi-data-value pi-font pi-border-color pi-item-spacing", attrs={"data-source": "BPM"})
for i in bpm:
    print(i.text)

# f = open("test.html", "a")
# f.write(soup.prettify())
# f.close()

# <td class="pi-horizontal-group-item pi-data-value pi-font pi-border-color pi-item-spacing" data-source="BPM">150</td>