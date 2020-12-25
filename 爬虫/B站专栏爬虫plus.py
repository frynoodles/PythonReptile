import 爬虫

tag = input('目标关键词:\n')
url = 'https://search.bilibili.com/article?keyword=' + tag
request = 爬虫.getRequest(url)
request.encoding = 'utf-8'
htmlurls = 爬虫.findall('<a title=".*?" href="(.*?)" target="_blank" class="title">', request.content.decode('utf-8'))
if len(htmlurls) == 0:
    print('没有相关专题')
else:
    for htmlurl in htmlurls:
        爬虫.biliArticleImgDownload('https:' + htmlurl, tag)
    print('任务完成')
