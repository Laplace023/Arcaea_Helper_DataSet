import requests
from bs4 import BeautifulSoup

songUrl = "https://arcwiki.mcd.blue/Testify"

def chartData():
    songHtml = requests.get(songUrl)
    soupHtml = BeautifulSoup(songHtml.content, 'html.parser')
    songData = soupHtml.find_all(class_="data")
    return(songData)

data = chartData()
print(data)
