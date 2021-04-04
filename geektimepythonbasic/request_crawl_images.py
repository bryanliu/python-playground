import os
import re
import shutil

import requests
from bs4 import BeautifulSoup
from threading import Thread

from geektimepythonbasic.Decorator_timer import timer


def downloadimage(imageurl, imagepath):
    """
    下载指定文件到指定目录
    :param imageurl:
    :param imagepath:
    :return:
    """
    print(f"start to download {imagepath}")
    resp = requests.get(imageurl, stream=True)
    if resp.status_code == 200:
        with open(imagepath, 'wb') as f:
            resp.raw.decode_content = True
            shutil.copyfileobj(resp.raw, f)
            print(f"end to download {imagepath}")


@timer
def geturl(url):
    content = requests.get(url[0])
    getcontent_re(content)


# print(content.text)
def getcontent_re(content):
    pattern = re.compile(r'<a href="(.*?)".*?title">(.*?)</div>', re.S)  # re.S 点匹配换行符
    # 匹配 图集的链接以及Title
    # 注意，这边的正则都要用到非贪婪模式，不然就会匹配到最后
    subpage = re.findall(pattern, content.text)
    # print(results)

    for res in subpage:
        # print(res)
        image, name = res
        name = re.sub('\s', '', name)
        # print(image, name)

    # 找出所有的<img 标记的图片，并且将jpg 后面的参数去掉。
    imgpattern = re.compile(r'<img src="(.*?jpg).*?".*?alt="(.*?)">', re.S)# re.S 点匹配换行符
    imgresult = re.findall(imgpattern, content.text)
    thread_list = []
    for res in imgresult:
        print(f"found picture {res}")
        # pass
        url, alt = res
        path = os.path.abspath("./downloadtmp")
        name = os.path.basename(url) #取出url中的最后一段，比如http://a/b/c.jpg, 最后会得到 c.jpg
        #print(name)
        imagepath = os.path.join(path, alt +".jpg")
        t = Thread(target=downloadimage, args=(url, imagepath))
        t.start()
        thread_list.append(t)
        #t.join() # 加了Join就不能并行执行了，Join的意思是先让这个线程执行完，再执行当前县城
        #downloadimage(url, os.path.join(path, name))
        #break
    for t in thread_list:
        t.join()


def getcontent_beautifulsoup(content):
    """
    使用 beautifulsoap解析内容
    # 使用 beautiful soap 拿到所有的image
    :param content:
    :return:
    """
    soup = BeautifulSoup(content.text, "lxml")
    images = soup.find_all('img')  # 注意是find下划线all, 不是 findall
    # print(images)
    # 效果和上面是类似的
    for img in images:
        print(img.get("src"), " | ", img.get("alt"))


url = "http://www.cnu.cc/discoveryPage/hot-风光"

if __name__ == "__main__":
    geturl(url)
