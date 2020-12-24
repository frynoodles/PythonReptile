import re
import os
import requests

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
}
url = input('请输入爬取目标URL：\n')
try:
    request = requests.get(url=url, headers=headers)
    request.encoding = "utf-8"
    data = request.content.decode('utf-8')
    title = re.findall('<h1 class="title">(.*?)</h1>\n', data)
    title = title[0]
    imgurls = re.findall('<figure class="img-box" contenteditable="false"><img data-src="(.*?)" width=".*?" height=".*?" data-size=".*?"/>',data)
    if not os.path.exists(title):
        os.mkdir(title)
    print(imgurls)
    for imgurl in imgurls:
        imgurl='https:'+imgurl
        picrequest = requests.get(url=imgurl, headers=headers)
        with open(title + '//' + imgurl[-20: ], 'wb+') as acti:
            acti.write(picrequest.content)
        acti.close()
        print(imgurl+'下载成功')
except BaseException:
    print('错误,请重试')
