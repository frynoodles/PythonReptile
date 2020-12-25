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
    try:
        request = getRequest(url)
        request.encoding = "utf-8"
        data = request.content.decode('utf-8')
        title = re.findall('<h1 class="title">(.*?)</h1>\n', data)
        title = title[0]
        imgurls = re.findall(
            '<img data-src="(.*?)" width=".*?" height=".*?" data-size=".*?"/>',
            data)
        imgurls2 = re.findall(
            '<img width=".*?" height=".*?" data-src=".*?" data-size=".*?" data-index=".*?" src="(.*?)" style="width: .*?; height: .*?;" class="loaded">',
            data)
        title = path + '//' + title
        if not os.path.exists(title):
            os.mkdir(title)
        for imgurl in imgurls:
            imgurl = 'https:' + imgurl
            picrequest = getRequest(imgurl)
            with open(title + '//' + imgurl[-20:], 'wb+') as acti:
                acti.write(picrequest.content)
            acti.close()
            print(imgurl + '下载成功')
        for imgurl in imgurls2:
            imgurl = 'https:' + imgurl
            picrequest = getRequest(imgurl)
            with open(title + '//' + imgurl[-20:], 'wb+') as acti:
                acti.write(picrequest.content)
            acti.close()
            print(imgurl + '下载成功')
        if len(imgurls) == len(imgurls2) == 0:
            print('该网页未检测到已添加匹配规则')
        print('○( ＾皿＾)っHiahiahia…  网页' + url + '爬取结束 ****')
    except BaseException:
        print('错误,请重试')
