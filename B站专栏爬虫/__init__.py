import re
import os
import requests


def findall(target, str):
    return re.findall(target, str)


def getRequest(url):
    return requests.get(url=url, headers=headers)


headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
}


def biliArticleImgDownload(url, path):
    if not os.path.exists(path):
        os.mkdir(path)

    request = getRequest(url)
    request.encoding = "utf-8"
    data = request.content.decode('utf-8')
    imgurls = re.findall(
        '<.*?img data-src="(.*?)".*?>',
        data)
    title = re.findall('https://www.bilibili.com/read/(.*?)\?from=search', url)
    title = path + '//' + title[0]
    if not os.path.exists(title):
        os.mkdir(title)
    for imgurl in imgurls:
        if 'https' not in imgurl:
            imgurl = 'https:' + imgurl
        picrequest = getRequest(imgurl)
        with open(title + '//' + imgurl[-20:], 'wb+') as acti:
            acti.write(picrequest.content)
        acti.close()
        print(imgurl + '下载成功')
    if len(imgurls) == 0:
        print('该网页未检测到已添加匹配规则')
    print('○( ＾皿＾)っHiahiahia…  网页' + url + '爬取结束 ****')
