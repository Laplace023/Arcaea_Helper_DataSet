import requests
from bs4 import BeautifulSoup
import csv

def chartConstant():
    songHtml = requests.get("https://arcwiki.mcd.blue/%E5%AE%9A%E6%95%B0%E8%AF%A6%E8%A1%A8")
    soupHtml = BeautifulSoup(songHtml.content, 'html.parser')
    songtr = soupHtml.find_all("tr")
    chartConstantLst = []
    chartConstantData = []
    for song in songtr:
        songStr = f'''{song}'''
        soupSongStr = BeautifulSoup(songStr, 'html.parser')
        chartConstantRaw = []
        for const in soupSongStr.find_all("td"):
            data = const.text
            chartConstantRaw.append(data)
        chartConstantLst.append(chartConstantRaw)
    for itemLst in chartConstantLst[1:]:
        song_dict = {}
        song_dict['Title'] = itemLst[0]
        song_dict['PST Const'] = itemLst[1]
        song_dict['PRS Const'] = itemLst[2]
        song_dict['FTR Const'] = itemLst[3]
        song_dict['BYD Const'] = itemLst[4]
        etr = itemLst[5]
        song_dict['ETR Const'] = etr[:-1]
        print(song_dict)
        chartConstantData.append(song_dict)
    return(chartConstantData)

song = chartConstant()
print(song)