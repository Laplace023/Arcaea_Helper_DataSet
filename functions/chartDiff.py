import requests
from bs4 import BeautifulSoup

def chartDiff(songUrl, diff):
    songHtml = requests.get(songUrl)
    soupHtml = BeautifulSoup(songHtml.content, 'html.parser')
    songDiff = soupHtml.find_all(class_=f"{diff}-data")
    songDiffLst = []
    songDiffDict = {}
    for song in songDiff:
        songText = song.text
        songDiffLst.append(songText)
    songDiffDict['Past Diff'] = songDiffLst[0]
    songDiffDict['Past Note Count'] = songDiffLst[1]
    songDiffDict['Past Chart Design'] = songDiffLst[2]
    return(songDiffDict)
