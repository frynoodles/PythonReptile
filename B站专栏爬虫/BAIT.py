import tkinter as tk
import B站专栏爬虫
import re
import os
import threading


pic: object = '''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'''


class myThread(threading.Thread):
    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name

    def run(self):
        getPic(tag.get())


def startthread():
    log('开始')
    thread = myThread(1, '123')
    thread.start()


i = 0
states: int = 0
window = tk.Tk()
# 标题
window.title('B站专栏图片爬虫工具')
# 窗口大小（长x宽）
window.geometry('500x350')

text = tk.Text('', width=20, height=20)
text.pack(fill=tk.X, side=tk.BOTTOM)


def biliArticleImgDownload(url, path):
    global i
    if not os.path.exists(path):
        os.mkdir(path)
    try:
        request = B站专栏爬虫.getRequest(url)
        request.encoding = "utf-8"
        data = request.content.decode('utf-8')
        title = re.findall('https://www.bilibili.com/read/(.*?)\?from=search', url)
        imgurls = re.findall(
            '<figure .*?class="img-box".*?><.*?img data-src="(.*?)".*?>',
            data)
        title = path + '//' + title[0]
        if not os.path.exists(title):
            os.mkdir(title)
        for imgurl in imgurls:
            if i == 1:
                break
            if 'https' not in imgurl:
                imgurl = 'https:' + imgurl
            picrequest = B站专栏爬虫.getRequest(imgurl)
            with open(title + '//' + imgurl[-20:], 'wb+') as acti:
                acti.write(picrequest.content)
            acti.close()
            log(imgurl + '下载成功')
        if len(imgurls) == 0:
            log('该网页未检测到已添加匹配规则')
        log('○( ＾皿＾)っHiahiahia…  网页' + url + '爬取结束 ****')
    except BaseException:
        log('错误,请重试')


def log(msg):
    text.insert(tk.END, msg + '\n')  # INSERT表示在光标位置插入
    text.see(tk.END)
    text.update()


log('B站专栏图片下载器')
log('在检索栏中输入关键词后按“搜索并下载“按钮开始下载')
log('将在软件同级目录下下载')

photo = tk.PhotoImage(data=pic)
text.image_create(tk.END, image=photo)  # 用这个方法创建一个图片对象，并插入到“END”的位置
text.pack()
log('')


def getPic(tag):
    global i
    if tag is not None:
        url = 'https://search.bilibili.com/article?keyword=' + tag
        request = B站专栏爬虫.getRequest(url)
        request.encoding = 'utf-8'
        htmlurls = B站专栏爬虫.findall('<a title=".*?" href="(.*?)" target="_blank" class="title">',
                                  request.content.decode('utf-8'))
        if len(htmlurls) == 0:
            log('没有相关专题')
        else:
            log('检索到第一页有' + str(len(htmlurls)) + '个专栏')
            for htmlurl in htmlurls:
                if i == 1:
                    break
                biliArticleImgDownload('https:' + htmlurl, tag)
            if len(htmlurls) < 20:
                log('即将下载完毕')
            else:
                log('推测专栏数大于20,开始下载后续专栏')
                n = 2
                while True:
                    if i == 1:
                        break
                    request = B站专栏爬虫.getRequest(url + str(n))
                    request.encoding = 'utf-8'
                    htmlurls = B站专栏爬虫.findall('<a title=".*?" href="(.*?)" target="_blank" class="title">',
                                              request.content.decode('utf-8'))
                    if len(htmlurls) == 0:
                        break
                    elif len(htmlurls) < 20:
                        for htmlurl in htmlurls:
                            if i == 1:
                                break
                            biliArticleImgDownload('https:' + htmlurl, tag)
                    else:
                        for htmlurl in htmlurls:
                            if i == 1:
                                break
                            biliArticleImgDownload('https:' + htmlurl, tag)
                    n += 1
        log('******结束******')
        i = 0
    else:
        log('请输入搜索关键词')


def stop():
    global i
    log('######################')
    log('收到指令，即将停止程序')
    log('######################')
    i = 1


tag = tk.Entry(window, show=None, font=('Arial', 14))

tag.pack()

b = tk.Button(window, text='搜索并下载', font=('Arial', 12), width=15, height=1,
              command=lambda: startthread(), activebackground='yellow')
b1 = tk.Button(window, text='停止程序', font=('Arial', 12), width=15, height=1,
               command=lambda: stop(), activebackground='red')
b.pack()
b1.pack()

# 循环刷新
window.mainloop()
