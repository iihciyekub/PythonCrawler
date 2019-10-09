import requests
from pyquery import PyQuery as pq

# 模拟请求头
headers = {
    "User-Agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36",
}


url = f'http://maoyan.com/board/6?offset=0'
html = requests.get(url, headers=headers).text

do = pq(html)

aa = do("#app .board-item-content").items()
for i in aa:
  print(i(".name a").attr("title"))
