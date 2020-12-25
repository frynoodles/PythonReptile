import 爬虫

tag = input('目标关键词:\n')
url = 'https://search.bilibili.com/article?keyword=' + tag
request = 爬虫.getRequest(url)
request.encoding = 'utf-8'
htmlurls = 爬虫.findall('<a title=".*?" href="(.*?)" target="_blank" class="title">', request.content.decode('utf-8'))
if len(htmlurls) == 0:
    print('没有相关专题')
else:
    print('检索到第一页有' + str(len(htmlurls)) + '个专栏')
    for htmlurl in htmlurls:
        爬虫.biliArticleImgDownload('https:' + htmlurl, tag)
    if len(htmlurls) < 20:
        print('下载完毕')
    else:
        print('推测专栏数大于20,开始下载后续专栏')
        n = 2
        while True:
            request = 爬虫.getRequest(url + str(n))
            request.encoding = 'utf-8'
            htmlurls = 爬虫.findall('<a title=".*?" href="(.*?)" target="_blank" class="title">',
                                  request.content.decode('utf-8'))
            if len(htmlurls) == 0:
                break
            elif len(htmlurls) < 20:
                for htmlurl in htmlurls:
                    爬虫.biliArticleImgDownload('https:' + htmlurl, tag)
            else:
                for htmlurl in htmlurls:
                    爬虫.biliArticleImgDownload('https:' + htmlurl, tag)
            n+=1
input('任务结束，请自行关闭')
