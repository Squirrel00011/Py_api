#软件工程后端

接口地址：http://139.159.143.46:8999

##接口

####1.歌名搜索

接口链接:
    
    http://139.159.143.46:8999/search_from_name/<music_name>
    <music_name>: 待搜索歌名，例如：new boy
    return: json格式数据，包含QQ 20首和网易云 20首，包括以下信息
    ID(id)、歌名(name)、歌手(artist)、唱片ID(albumID)、唱片名(albumName)、唱片图片链接(albumPic,若没有返回NULL)、发布时间(publicTime,时间戳形式,需要转换)

样例：

    http://139.159.143.46:8999/search_from_name/new boy

return: 
    
    {"count": 40, "NC": [{"id": 1857630559, "name": "New Boy", "artist": "房东的猫", "albumID": 128805937, "albumName": "谁是宝藏歌手 第8期", "albumPic": "http://p3.music.126.net/KkrcSwKbRsd8GuaOHILlxA==/109951166077317301.jpg", "publicTime": 1623340800000}, {"id": 139371, "name": "New Boy", "artist": "朴树", "albumID": 13892, "albumName": "我去2000年", "albumPic": "http://p3.music.126.net/XC_KCBokxczQjq0asRBsbQ==/109951166118038905.jpg", "publicTime": 915120000000}, {"id": 1875525832, "name": "New boy（房东的猫）", "artist": "冰美式不加糖", "albumID": 132788873, "albumName": "New boy（房东的猫）", "albumPic": "http://p3.music.126.net/62tJByrnzYUkPb4UqhLmLA==/109951166356386117.jpg", "publicTime": 0}, {"id": 28996919, "name": "NEW BOY", "artist": "朴树", "albumID": 2975136, "albumName": "我去2000年", "albumPic": "http://p3.music.126.net/_BouIwtRdgCnauROu7vlpw==/109951166457116553.jpg", "publicTime": 1064592000000}, {"id": 1855977953, "name": "NewBoy （抖音完整现场版）", "artist": "小郗", "albumID": 127368025, "albumName": "暖", "albumPic": "http://p3.music.126.net/ZnMrv37FSAGLroyBP8WBuA==/109951165976463713.jpg", "publicTime": 0}, {"id": 1928411190, "name": "New Boy（甜美女声版）", "artist": "王可可", "albumID": 141849534, "albumName": "NewBoy", "albumPic": "http://p4.music.126.net/3zau2mWB214CTd1c42hOiw==/109951167152353744.jpg", "publicTime": 0}, {"id": 1921230306, "name": "new boy", "artist": "浅影阿", "albumID": 140562767, "albumName": "浅影的翻唱合集", "albumPic": "http://p3.music.126.net/yrSnflc8XIRY5Hjgkoka1Q==/109951167061133615.jpg", "publicTime": 0}, {"id": 1934956041, "name": "NEW BOY", "artist": "李冠霖YoungLegend", "albumID": 142958521, "albumName": "NEW BOY", "albumPic": "http://p4.music.126.net/6VHzOl9thVifaI7tFoby4w==/109951167242528042.jpg", "publicTime": 0}, {"id": 1943886292, "name": "New Boy (cover 盘尼西林)", "artist": "Megalen", "albumID": 144343451, "albumName": "Cover集合", "albumPic": "http://p3.music.126.net/i73whIUxAb76o8FGxNgghA==/109951167370154217.jpg", "publicTime": 0}, {"id": 1924862909, "name": "New Boy", "artist": "谷雨萌", "albumID": 141213046, "albumName": "New Boy", "albumPic": "http://p3.music.126.net/lQVzBvtHdiogerOVmhX-Og==/109951167108577499.jpg", "publicTime": 0}, {"id": 1869665021, "name": "New Boy", "artist": "尤大爷", "albumID": 131801154, "albumName": "New Boy", "albumPic": "http://p3.music.126.net/t48Nh6ufVNmDrJ2VE1ITEg==/109951166285576282.jpg", "publicTime": 0}, {"id": 1896996594, "name": "NEW BOY", "artist": "微许", "albumID": 136429263, "albumName": "NEW BOY", "albumPic": "http://p4.music.126.net/8PQ5CzfmtnWrPMxDVF2aZw==/109951166646551816.jpg", "publicTime": 0}, {"id": 1945573309, "name": "new boy（吉他弹唱）", "artist": "微甜的小风", "albumID": 143593784, "albumName": "只道寻常", "albumPic": "http://p4.music.126.net/hb8C2SXutVFp-rbA8epzhw==/109951167302697245.jpg", "publicTime": 0}, {"id": 1881535755, "name": "New Boy", "artist": "九三", "albumID": 129627118, "albumName": "九三的翻唱", "albumPic": "http://p3.music.126.net/1PJVvj5b_sL5tPl9K1L_vw==/109951166128941310.jpg", "publicTime": 0}, {"id": 1945319339, "name": "New boy（钢琴版）", "artist": "海上钢琴狮", "albumID": 143919829, "albumName": "钢琴流行作品演绎", "albumPic": "http://p4.music.126.net/kC6-etSwD5DzLg1gPskUDQ==/109951167334675814.jpg", "publicTime": 0}, {"id": 1407675159, "name": "new boy", "artist": "赵睿", "albumID": 83801584, "albumName": "翻唱", "albumPic": "http://p4.music.126.net/ksLnQjDm4_3M7Xk7RHgAJQ==/109951164528773273.jpg", "publicTime": 0}, {"id": 1883937504, "name": "New Boy", "artist": "小谢同学", "albumID": 91852693, "albumName": "七月一日", "albumPic": "http://p4.music.126.net/pLN3K6Kz9fi1SzdWuwjN-w==/109951165106969668.jpg", "publicTime": 0}, {"id": 1945277475, "name": "New Boy", "artist": "娜娜的信", "albumID": 144615499, "albumName": "New Boy", "albumPic": "http://p3.music.126.net/6bz1fFIDmkZYarL1wUYAeQ==/109951167386418362.jpg", "publicTime": 0}, {"id": 1881225995, "name": "New Boy", "artist": "陈阳", "albumID": 133780664, "albumName": "阳阳的弹唱第二十六弹", "albumPic": "http://p4.music.126.net/vZoqpWbZyFjBcGmB0pqcRw==/109951166454195506.jpg", "publicTime": 0}, {"id": 1475791050, "name": "Boys", "artist": "Lizzo", "albumID": 94809016, "albumName": "New Pop Hits", "albumPic": "http://p4.music.126.net/P_RXx9uasPYBGZfNGsnyyg==/109951165288916427.jpg", "publicTime": 1599148800000}], "QQ": [{"id": "003UTVCN0QvffG", "name": "New Boy", "artist": "房东的猫", "albumID": "002uI8vg4QBFEY", "albumName": "New Boy", "albumPic": "http://y.qq.com/music/photo_new/T002R300x300M000002uI8vg4QBFEY_1.jpg?max_age=2592000", "publicTime": 1627315206}, {"id": "002ic6jw1iwaBn", "name": "NEW BOY", "artist": "朴树", "albumID": "001n8QT30kOhTD", "albumName": "我去2000年", "albumPic": "http://y.qq.com/music/photo_new/T002R300x300M000001n8QT30kOhTD_1.jpg?max_age=2592000", "publicTime": 915120000}, {"id": "000Trxqh2b4I8N", "name": "New Boy (Live)", "artist": "谭松韵", "albumID": "", "albumName": "", "albumPic": "NULL", "publicTime": 0}, {"id": "0031fzjl4PMXru", "name": "New Boy (Live)", "artist": "盘尼西林乐队", "albumID": "001HWIt70hEXzV", "albumName": "乐队的夏天 第5期", "albumPic": "http://y.qq.com/music/photo_new/T002R300x300M000001HWIt70hEXzV_2.jpg?max_age=2592000", "publicTime": 1561132800}, {"id": "001s4iag4Oihut", "name": "《New Boy》房东的猫、陈婧霏：新世界来的像梦一样 让我暖洋洋 (节目)", "artist": "卿听盲盒", "albumID": "002DJazZ4TlWbm", "albumName": "音乐星舞台", "albumPic": "http://y.qq.com/music/photo_new/T002R300x300M000002DJazZ4TlWbm_2.jpg?max_age=2592000", "publicTime": 1644459815}, {"id": "001R5CHU1QaHrZ", "name": "New Boy (伴奏)", "artist": "房东的猫", "albumID": "002uI8vg4QBFEY", "albumName": "New Boy", "albumPic": "http://y.qq.com/music/photo_new/T002R300x300M000002uI8vg4QBFEY_1.jpg?max_age=2592000", "publicTime": 1627315205}, {"id": "000TrOzi3YWzXC", "name": "New boy (Live)", "artist": "欧阳娜娜", "albumID": "0033furw1sIQym", "albumName": "幸福合家欢 2020江苏卫视春晚", "albumPic": "http://y.qq.com/music/photo_new/T002R300x300M0000033furw1sIQym_1.jpg?max_age=2592000", "publicTime": 1579881600}, {"id": "000Z9MKH2s4S1k", "name": "New Boy (完整女声版)", "artist": "李莹小熊", "albumID": "004Rzwix2jajdH", "albumName": "天籁之音", "albumPic": "http://y.qq.com/music/photo_new/T002R300x300M000004Rzwix2jajdH_1.jpg?max_age=2592000", "publicTime": 1620057600}, {"id": "001SwnHO0YTLIY", "name": "New Boy (remix: 房东的猫)", "artist": "DJMonk", "albumID": "001485WF24ZUBv", "albumName": "房东的猫 - New Boy DJMonk版", "albumPic": "http://y.qq.com/music/photo_new/T002R300x300M000001485WF24ZUBv_1.jpg?max_age=2592000", "publicTime": 1643726762}, {"id": "002Vh3Yz2Bn3IF", "name": "New Boy (纯音乐)", "artist": "朴树", "albumID": "", "albumName": "", "albumPic": "NULL", "publicTime": 0}, {"id": "004B9uO32qwKZf", "name": "New Boy （小提琴）", "artist": "时光", "albumID": "001cHhhq4PYfNp", "albumName": "New Boy", "albumPic": "http://y.qq.com/music/photo_new/T002R300x300M000001cHhhq4PYfNp_1.jpg?max_age=2592000", "publicTime": 1635753063}, {"id": "002S6NM61tmUg5", "name": "NEW BOY", "artist": "DJ.AY", "albumID": "002cVPz14WXxS1", "albumName": "NEW BOY", "albumPic": "http://y.qq.com/music/photo_new/T002R300x300M000002cVPz14WXxS1_2.jpg?max_age=2592000", "publicTime": 1629115143}, {"id": "000mKn0p0qsN0g", "name": "《new boy》抖音版：快乐在城市上空飘扬 (节目)", "artist": "音乐全能鹅", "albumID": "003QvKYG3U3FDk", "albumName": "音乐✨舞台", "albumPic": "http://y.qq.com/music/photo_new/T002R300x300M000003QvKYG3U3FDk_1.jpg?max_age=2592000", "publicTime": 1628653952}, {"id": "0044XXZa2OKor5", "name": "New Boy", "artist": "小钳子", "albumID": "0002Gjhi2qmbIE", "albumName": "可甜可盐小钳子翻唱专辑", "albumPic": "http://y.qq.com/music/photo_new/T002R300x300M0000002Gjhi2qmbIE_4.jpg?max_age=2592000", "publicTime": 1582128000}, {"id": "003iIKao4P7K2H", "name": "New Boy", "artist": "李亿安", "albumID": "003WcXEs0A5C95", "albumName": "1234", "albumPic": "http://y.qq.com/music/photo_new/T002R300x300M000003WcXEs0A5C95_1.jpg?max_age=2592000", "publicTime": 1651843022}, {"id": "002sB4nX3JxgsL", "name": "New Boy (网络版)", "artist": "小抖", "albumID": "000rdjCd2JyFR5", "albumName": "神魂颠倒", "albumPic": "http://y.qq.com/music/photo_new/T002R300x300M000000rdjCd2JyFR5_1.jpg?max_age=2592000", "publicTime": 1639670480}, {"id": "003g6YCe3sRLGN", "name": "New Boy (Live)", "artist": "朴树", "albumID": "000j0jDK0PrQMN", "albumName": "恒大星光音乐节", "albumPic": "http://y.qq.com/music/photo_new/T002R300x300M000000j0jDK0PrQMN_1.jpg?max_age=2592000", "publicTime": 1410969600}, {"id": "003yCmVR3lggry", "name": "New Boy", "artist": "颜妹", "albumID": "002P3Ttg26geOn", "albumName": "普通爱情故事", "albumPic": "http://y.qq.com/music/photo_new/T002R300x300M000002P3Ttg26geOn_1.jpg?max_age=2592000", "publicTime": 1632412800}, {"id": "003lr5Vr1ThSzC", "name": "New Boy（Live）", "artist": "朴树", "albumID": "", "albumName": "", "albumPic": "NULL", "publicTime": 0}, {"id": "000ZuZsZ4Bqdto", "name": "New Boy", "artist": "橙大蕾蕾", "albumID": "000YkY9e3Z7Enl", "albumName": "New Boy", "albumPic": "http://y.qq.com/music/photo_new/T002R300x300M000000YkY9e3Z7Enl_1.jpg?max_age=2592000", "publicTime": 1628656562}]}

####2.ID搜索

接口链接:
    
    http://139.159.143.46:8999/get_url_from_id/<PT>/<music_id>
    <PT>: 音乐平台(NC：网易云音乐，QQ：QQ音乐)，例如：NC
    <music_id>: 待播放歌曲的ID，例如：28996919
    return: 歌曲的url链接，可直接播放

样例: 

    http://139.159.143.46:8999/get_url_from_id/NC/28996919

return: 

    http://m701.music.126.net/20220509114007/bdd479db2d77b41e2b52fa69bd804b65/jdymusic/obj/wo3DlMOGwrbDjj7DisKw/8360324650/a226/2a98/17af/eb763cf8df3f7615b85b0bbb578e0096.mp3

样例:

    http://139.159.143.46:8999/get_url_from_id/QQ/003UTVCN0QvffG

return:

    http://isure.stream.qqmusic.qq.com/C400003UTVCN0QvffG.m4a?guid=2796982635&vkey=DCBD3739413CD39C1008D0D95812F6427663BBCE9689AC49E2EF78913189B9BCE12C1BA6AC528366778AAF364A03BD37BFF38615E6ACB116&uin=&fromtag=120002


####3.获取歌词

接口连接：

    http://192.168.1.102:8080/get_lyric_from_id/<PT>/<music_id>
    <PT>: 音乐平台(NC：网易云音乐，QQ：QQ音乐)，例如：NC
    <music_id>：待查找歌曲ID，例如：28996919
    return：歌曲的带时间戳歌词

样例：

    http://139.159.143.46:8999/get_lyric_from_id/NC/28996919

return: 

    [00:00.000] 作词 : 朴树 [00:01.000] 作曲 : 朴树 [00:02.000] 编曲 : 张亚东 [00:03.000] 制作人 : 张亚东 [00:06.99]是的我看见到处是阳光 [00:11.02]快乐在城市上空飘扬 [00:14.61]新世纪来得像梦一样 [00:18.23]让我暖洋洋 [00:21.82]你的老怀表还在转吗 [00:25.40]你的旧皮鞋还能穿吗 [00:29.03]这儿有一支未来牌香烟 [00:32.64]你不想尝尝吗 [00:35.84]明天一早 [00:39.38]我猜阳光会好 [00:43.49]我要把自己打扫 [00:47.02]把破旧的全部卖掉 [00:49.99]哦这样多好 [00:54.21]快来吧奔腾电脑 [00:57.89]就让它们代替我来思考 [01:04.25]穿新衣吧剪新发型呀 [01:08.27]轻松一下WINDOWS98 [01:11.84]打扮漂亮 [01:13.60]18岁是天堂 [01:15.60]我们的生活甜得像糖 [01:19.12]穿新衣吧剪新发型呀 [01:22.63]轻松一下WINDOWS98 [01:26.34]以后的路不再会有痛苦 [01:29.97]我们的未来该有多酷 [01:34.53] [02:02.45]明天一早 [02:06.46]我猜阳光会好 [02:10.13]我要把自己打扫 [02:13.66]把破旧的全部卖掉 [02:16.54]哦这样多好 [02:20.89]快来吧奔腾电脑 [02:24.53]就让它们代替我来思考 [02:31.35]穿新衣吧剪新发型呀 [02:34.84]轻松一下WINDOWS98 [02:38.52]打扮漂亮 [02:40.28]18岁是天堂 [02:42.20]我们的生活甜得像糖 [02:45.76]穿新衣吧剪新发型呀 [02:49.28]轻松一下WINDOWS98 [02:52.96]以后的路不再会有痛苦 [02:56.64]我们的未来该有多酷 [03:00.25]BABAWOWO... [03:07.40]向前走你的路 [03:10.92]猜猜未来给你什么礼物 [03:14.65]BABAWOWO... [03:21.90]扔掉吧你的旧书包 [03:25.93]OH MY INTERNATIONAL COOL PLAY BOY [03:30.05]