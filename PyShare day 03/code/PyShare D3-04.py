"""
异步爬虫库,aiohttp的使用
更多内容:https://aiohttp.readthedocs.io/en/stable/client_quickstart.html#make-a-request

"""

import requests
import time

url = [i for i in range(5)]
url[0] = "http://maoyan.com/board/1"
url[1] = "http://maoyan.com/board/2"
url[2] = "http://maoyan.com/board/4"
url[3] = "http://maoyan.com/board/5"
url[4] = "http://maoyan.com/board"

# reques5ts 请求头
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36"
}


def fun(url):
    a = requests.get(url, headers=headers)
    return a.text


start = time.time()

result = []
for i in url:
    result.append(fun(i))

print(result[3])

print(time.time() - start)
