import requests
from bs4 import BeautifulSoup
import csv

url = "https://arcwiki.mcd.blue"
r = requests.get("https://arcwiki.mcd.blue/%E5%AE%9A%E6%95%B0%E8%AF%A6%E8%A1%A8")

# Parsing the HTML
soup = BeautifulSoup(r.content, 'html.parser')

song = soup.find_all("tr")
song_list = []
song_list2 = []
data_final1 = []
for song2 in song:
    x = f'''{song2}'''
    song_data = []
    sp = BeautifulSoup(x, 'html.parser')
    for link in sp.find_all("a", href = True):
        hreflink = link['href']
        url2 = url + hreflink
        print(url2)
        song_list.append(url2)
    for const in sp.find_all("td"):
        data = const.text
        song_data.append(data)
        song_dict = {}
    song_list2.append(song_data)

print(song_list2)
for songs in song_list2[1:]:
    song_dict = {}
    song_dict['title'] = songs[0]
    song_dict['pst'] = songs[1]
    song_dict['prs'] = songs[2]
    song_dict['ftr'] = songs[3]
    song_dict['byd'] = songs[4]
    etr = songs[5]
    song_dict['etr'] = etr[:-1]
    print(song_dict)
    data_final1.append(song_dict)

with open('table1.csv', 'w', newline='') as csvfile:
    fieldnames = ['title', 'pst', 'prs', 'ftr', 'byd', 'etr']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data_final1)


#song data

# for url3 in song_list:
#    r = requests.get(url3)
#    soup = BeautifulSoup(r.content, 'html.parser')
#
#    song = soup.find_all(class_="data")
#    for s in song:
#        print(s.text)
#    pst = soup.find_all(class_="pst-data")
#   for x in pst:
#        print(x.text)