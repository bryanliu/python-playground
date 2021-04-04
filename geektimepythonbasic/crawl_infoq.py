import requests
from bs4 import BeautifulSoup

"""
infoq 改版了，现在都没有静态的资源了，代码写一下，就当练手吧。
换了http://gaoqing.la/ 试手.
将http://gaoqing.la/1080p/page/ 所有的page 都抓一下，抓取电源的名字和详情页连接。
PS：一共有多少页需要手动看一下。
"""

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.8",
    "Connection": "close",
    "Cookie": "_gauges_unique_hour=1; _gauges_unique_day=1; _gauges_unique_month=1; _gauges_unique_year=1; _gauges_unique=1",
    "Referer": "http://www.infoq.com",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36 LBBROWSER"
}

url = "http://gaoqing.la/1080p/page/"


def crawlurl(url):
    content = requests.get(url, headers=headers)
    # print(content.text)
    soup = BeautifulSoup(content.text, "lxml")
    # 将所有 class 为 news_type_block 的div 都搜出来，在最新的soup中，class 得用class_ 来标示
    for news in soup.find_all("div", class_='thumbnail'):
        # 获得title 和详情页的地址列表
        print([(title.get('title'), title.get('href')) for title in news.find_all('a') if title.get('title')])


for i in range(1, 2):  # 2021-04-04 一共是13页，如果都下载，稍微要花点时间，默认下载第一页。
    crawlurl(url + str(i))
