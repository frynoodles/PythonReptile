import tkinter as tk
import B站专栏爬虫
import re
import os
import threading


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


log('Bz站专栏图片下载器')
log('在检索栏中输入关键词后按“搜索并下载“按钮开始下载')
log('将在软件同级目录下下载')
photo = tk.PhotoImage(file='CN_bilibili B.png')
text.image_create(tk.END, image=photo)  # 用这个方法创建一个图片对象，并插入到“END”的位置
text.pack()


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
