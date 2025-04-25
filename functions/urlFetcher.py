import requests
from bs4 import BeautifulSoup

def urlFetcher():
    baseUrl = "https://arcwiki.mcd.blue"
    songHtml = requests.get("https://arcwiki.mcd.blue/%E5%AE%9A%E6%95%B0%E8%AF%A6%E8%A1%A8")
    soupHtml = BeautifulSoup(songHtml.content, 'html.parser')
    songtr = soupHtml.find_all("tr")
    songUrl = []
    for song in songtr:
        songStr = f'''{song}'''
        soupSongStr = BeautifulSoup(songStr, 'html.parser')
        for affix in soupSongStr.find_all("a", href = True):
            affixUrl = affix['href']
            fullUrl = baseUrl + affixUrl
            songUrl.append(fullUrl)
    return(songUrl)

data = urlFetcher()
print(data)