import requests
from pyquery import PyQuery as pq

# 模拟请求头
headers = {
    "User-Agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36",
}

#用函数构造网页
def urlw(indext):
    return f'http://maoyan.com/board/6?offset={str(indext)}'


for i in range(1, 100, 10):
    html = requests.get(urlw(i), headers=headers)
    do = pq(html.text)
    aa = do("#app .board-item-content").items()
    for i in aa:
        print(i(".name a").attr("title"))
