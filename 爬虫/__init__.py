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


def download(url, path):
    if not os.path.exists(path):
        os.mkdir(path)
    try:
        request = getRequest(url)
        request.encoding = "utf-8"
        data = request.content.decode('utf-8')
        title = re.findall('<h1 class="title">(.*?)</h1>\n', data)
        title = title[0]
        imgurls = re.findall(
            '<figure class="img-box" contenteditable="false"><img data-src="(.*?)" width=".*?" height=".*?" data-size=".*?"/>',
            data)
        title = path + '//' + title
        if not os.path.exists(title):
            os.mkdir(title)
        print(imgurls)
        for imgurl in imgurls:
            imgurl = 'https:' + imgurl
            picrequest = getRequest(imgurl)
            with open(title + '//' + imgurl[-20:], 'wb+') as acti:
                acti.write(picrequest.content)
            acti.close()
            print(imgurl + '下载成功')
        print('**** 任务' + url + '完成 ****')
    except BaseException:
        print('错误,请重试')
