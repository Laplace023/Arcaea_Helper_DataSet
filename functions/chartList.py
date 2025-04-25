import requests
from bs4 import BeautifulSoup

def chartList():
    baseUrl = "https://arcwiki.mcd.blue"
    songHtml = requests.get("https://arcwiki.mcd.blue/%E5%AE%9A%E6%95%B0%E8%AF%A6%E8%A1%A8")
    soupHtml = BeautifulSoup(songHtml.content, 'html.parser')
    songtr = soupHtml.find_all("tr")
    chartConstantLst = []
    chartConstantData = []
    songUrl = []
    for song in songtr:
        songStr = f'''{song}'''
        soupSongStr = BeautifulSoup(songStr, 'html.parser')
        chartConstantRaw = []
        for const in soupSongStr.find_all("td"):
            data = const.text
            chartConstantRaw.append(data)
        chartConstantLst.append(chartConstantRaw)
    for song in songtr:
        songStr = f'''{song}'''
        soupSongStr = BeautifulSoup(songStr, 'html.parser')
        for affix in soupSongStr.find_all("a", href = True):
            affixUrl = affix['href']
            fullUrl = baseUrl + affixUrl
            songUrl.append(fullUrl)
    for itemLst, url in zip(chartConstantLst[1:], songUrl):
        song_dict = {}
        song_dict['Title'] = itemLst[0]
        song_dict['Url'] = url
        song_dict['PST Const'] = itemLst[1]
        song_dict['PRS Const'] = itemLst[2]
        song_dict['FTR Const'] = itemLst[3]
        song_dict['BYD Const'] = itemLst[4]
        etr = itemLst[5]
        song_dict['ETR Const'] = etr[:-1]
        chartConstantData.append(song_dict)
    return(chartConstantData)
