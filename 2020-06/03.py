import urllib.request
from urllib.error import URLError
import os
import re
import ssl
import  socket

socket.setdefaulttimeout(20)
def urlopen(url):

    context = ssl._create_unverified_context()
    # req = urllib.request.Request(url)
    # req.add_header('user-agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36')
    headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "accept-language": "zh-CN,zh;q=0.9",
        "cache-control": "no-cache",
        "pragma": "no-cache",
        "referer": "https://yiren91.com/",
        "upgrade-insecure-requests": 1,
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"
    }
    req = urllib.request.Request(url,headers=headers)
    response = urllib.request.urlopen(req,context=context)
    html = response.read()
    return html

def get_page(url):
    html = urlopen(url).decode('utf-8')
    P = r'<li><a href="(/se/zhenshizipai/[+\d]+\.html)'
    pagesList = re.findall(P,html)
    # print(pagesList)
    # for each in pagesList:
    #     print(each)
    return pagesList

def find_imgs(url):
    # print(url)
    html = urlopen(url).decode('utf-8')
    p = r'<img id="aimg_[a-z0-9A-z]+" src="([a-zA-z]+://[^\s]*\.jpg)'
    # print('html:',html)
    img_addrs = re.findall(p,html)
    # print('img：',img_addrs)
    if len(img_addrs) != 0:
        return img_addrs


def save_imgs(folder,img_addrs):
    for i in img_addrs:
        try:
            html = urlopen(i)
            filename = i.split('/')[-1]
            print(i)
            with open(filename,'wb') as f:
                f.write(html)
        except Exception as e:
            print(i,e)


def download_mm(folder='ooxx',pages=10):
    if not os.path.exists('ooxx'):
        os.mkdir(folder)
    os.chdir(folder)

    url = 'https://yiren91.com/se/zhenshizipai/'
    # a = urlopen(url).decode("utf8","ignore")
    # print(a)
    pages = get_page(url)
    # print(pages)
    for i in pages:
        pageurl = 'https://yiren91.com' + i
        try:
            print(pageurl)
            imglist=find_imgs(pageurl)
            if imglist:
                save_imgs(folder,imglist)
        except Exception as e:
            print(e)
        except URLError as ue:
            print(ue)
if __name__ == '__main__':
    download_mm()