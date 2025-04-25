import requests
from bs4 import BeautifulSoup
import csv

from functions import chartList
from functions import chartData

chartLst = chartList.chartList()
chartCompileList = []
for compile in chartLst:
    songDict = dict(compile)
    url = songDict['Url']
    data = chartData.chartData(url)
    songDict.update(data)
    print(songDict)
    chartCompileList.append(songDict)

with open('songData.csv', 'w', newline='') as csvfile:
    fieldnames = ['Title', 'Artist', 'Duration', 'BPM', 'Release', 'PST Const', 'pst', 'pst Note Count', 'pst Chart Design', 'PRS Const', 'prs', 'prs Note Count', 'prs Chart Design', 'FTR Const', 'ftr', 'ftr Note Count', 'ftr Chart Design', 'BYD Const', 'byd', 'byd Note Count', 'byd Chart Design', 'ETR Const', 'etr', 'etr Note Count', 'etr Chart Design', 'Url']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(chartCompileList)
