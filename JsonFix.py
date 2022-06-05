import json
import requests
#歌名、歌手、专辑、时间

url_api_QQA = "http://139.159.143.46:3300" #QQ音乐接口

def NC_QQ_Json(NC_music_list, QQ_music_list):
    NC_QQ_list = {}
    count = 40
    NC_QQ_list["count"] = count#网易云 20，QQ音乐 20
    NC_QQ_list["NC"] = []
    NC_QQ_list["QQ"] = []
    for i in range((int)(count/2)):
        NC_list = {}
        QQ_list = {}
        #------网易云音乐接口处理------#
        NC_list["id"] = NC_music_list["result"]["songs"][i]["id"]#获取歌曲ID
        NC_list["name"] = NC_music_list["result"]["songs"][i]["name"]#获取歌名
        NC_list["artist"] = NC_music_list["result"]["songs"][i]["ar"][0]["name"]#获取歌手姓名
        NC_list["albumID"] = NC_music_list["result"]["songs"][i]["al"]["id"]#获取专辑ID
        NC_list["albumName"] = NC_music_list["result"]["songs"][i]["al"]["name"]#获取专辑名称
        NC_list["albumPic"] = NC_music_list["result"]["songs"][i]["al"]["picUrl"]#获取唱片封面
        NC_list["publicTime"] = NC_music_list["result"]["songs"][i]["publishTime"]#获取发布时间

        #------QQ音乐接口处理------#
        QQ_list["id"] = QQ_music_list["data"]["list"][i]["songmid"]#获取歌曲ID
        QQ_list["name"] = QQ_music_list["data"]["list"][i]["songname"]#获取歌名
        QQ_list["artist"] = QQ_music_list["data"]["list"][i]["singer"][0]["name"]#获取歌手姓名
        QQ_list["albumID"] = QQ_music_list["data"]["list"][i]["albummid"]#获取专辑ID
        QQ_list["albumName"] = QQ_music_list["data"]["list"][i]["albumname"]#获取专辑名称

        url = url_api_QQA + "/album?albummid=" + QQ_list["albumID"]#获取唱片封面
        albumPic = requests.get(url).json()
        if("data" in albumPic):
            QQ_list["albumPic"] = "http:" + albumPic["data"]["picurl"]
        else:
            QQ_list["albumPic"] = "NULL"

        QQ_list["publicTime"] = QQ_music_list["data"]["list"][i]["pubtime"]#获取发布时间
        #------结果合并------#
        NC_QQ_list["NC"].append(NC_list)
        NC_QQ_list["QQ"].append(QQ_list)
    return NC_QQ_list