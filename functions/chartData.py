import requests
from bs4 import BeautifulSoup


def chartData(songUrl):
    def chartDiff(diff):
        songDiff = soupHtml.find_all(class_=f"{diff}-data")
        songDiffLst = []
        songDiffDict = {}
        for song in songDiff:
            songText = song.text
            songDiffLst.append(songText)
        songDiffDict[f'{diff}'] = songDiffLst[0]
        songDiffDict[f'{diff} Note Count'] = songDiffLst[1]
        songDiffDict[f'{diff} Chart Design'] = songDiffLst[2]
        return(songDiffDict)
    
    def chartExtra():
        songDiff = soupHtml.find_all(class_=f"byd-data")
        songExtraLst = []
        songExtraDict = {}
        for song in songDiff:
            songText = song.text
            songExtraLst.append(songText)
        songByd = soupHtml.find_all(class_="byd-label")
        songEtr = soupHtml.find_all(class_="etr-label")
        if len(songByd) == 0:
            songExtraDict['byd'] = ""
            songExtraDict['byd Note Count'] = ""
            songExtraDict['byd Chart Design'] = ""
        else:
            try:
                if songExtraLst[1] == "空":
                    songExtraDict['byd'] = ""
                    songExtraDict['byd Note Count'] = ""
                    songExtraDict['byd Chart Design'] = ""
                else:
                    songExtraDict['byd'] = songExtraLst[0]
                    songExtraDict['byd Note Count'] = songExtraLst[1]
                    songExtraDict['byd Chart Design'] = songExtraLst[2]
            except:
                songExtraDict['byd'] = 'TBA'
                songExtraDict['byd Note Count'] = 'TBA'
                songExtraDict['byd Chart Design'] = 'TBA'
        if len(songEtr) == 0:
            songExtraDict['etr'] = ""
            songExtraDict['etr Note Count'] = ""
            songExtraDict['etr Chart Design'] = ""
        else:
            songExtraDict['etr'] = songExtraLst[0]
            songExtraDict['etr Note Count'] = songExtraLst[1]
            songExtraDict['etr Chart Design'] = songExtraLst[2]
        return(songExtraDict)
    
    songHtml = requests.get(songUrl)
    soupHtml = BeautifulSoup(songHtml.content, 'html.parser')
    songData = soupHtml.find_all(class_="data")
    songDataLst = []
    songDataDict = {}
    for song in songData:
        songText = song.text
        songDataLst.append(songText)

    songPst = chartDiff("pst")
    songPrs = chartDiff("prs")
    songFtr = chartDiff("ftr")
    songExtra = chartExtra()

    songDataDict['Artist'] = songDataLst[0]
    songDataDict['Duration'] = songDataLst[2]
    songDataDict['BPM'] = songDataLst[3]
    release = songDataLst[4]
    songDataDict['Release'] = release[3:]
    songDataDict.update(songPst)
    songDataDict.update(songPrs)
    songDataDict.update(songFtr)
    songDataDict.update(songExtra)
    return(songDataDict)
