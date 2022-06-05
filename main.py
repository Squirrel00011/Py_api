import json
import requests
import flask
import JsonFix
url_api_NCA = "http://139.159.143.46:3000" #网易云接口
url_api_QQA = "http://139.159.143.46:3300" #QQ音乐接口
BackHost  = "192.168.0.101"#后端地址
port = "8999" #后端端口

app = flask.Flask(__name__)
app.config.from_pyfile("config.ini")

@app.route("/search_from_name/<music_name>")
def search_from_name(music_name):
    print(music_name)
    #网易云
    url = url_api_NCA + "/cloudsearch?keywords=" + music_name#拼接查询地址
    NC_music_list = requests.get(url).json()#获得网易云接口返回json文件
    #QQ音乐
    url = url_api_QQA + "/search?key=" + music_name#拼接查询地址
    QQ_music_list = requests.get(url).json()  # 获得QQ音乐接口返回json文件
    NC_QQ_list = JsonFix.NC_QQ_Json(NC_music_list,QQ_music_list)
    return json.dumps(NC_QQ_list,ensure_ascii=False)

@app.route("/get_url_from_id/<PT>/<music_id>")
def get_url_from_id(PT, music_id):
    print(PT, music_id)
    if PT=="NC":
        url = url_api_NCA + "/song/url?id=" + music_id
        music_url = requests.get(url).json()
        return music_url["data"][0]["url"]
    elif PT=="QQ":
        url = url_api_QQA + "/song/urls?id=" + music_id
        music_url = requests.get(url).json()
        return music_url["data"][music_id]
    else:
        return "平台错误"

@app.route("/get_lyric_from_id/<PT>/<music_id>")
def get_lyric_from_id(PT, music_id):
    print(PT, music_id)
    if PT=="NC":
        url = url_api_NCA + "/lyric?id=" + music_id
        lyric = requests.get(url).json()
        return json.dumps(lyric["lrc"]["lyric"],ensure_ascii=False)
    elif PT=="QQ":
        url = url_api_QQA + "/lyric?songmid=" + music_id
        lyric = requests.get(url).json()
        return json.dumps(lyric["data"]["lyric"], ensure_ascii=False)

def main():
    print(search_from_name("告白气球"))
    return

if __name__ == "__main__":
    app.debug = True
    #测试
    app.run(host="192.168.1.101",port="8081")
    #实际
    # app.run(host=BackHost, port=port)