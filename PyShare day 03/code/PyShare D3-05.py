"""
异步爬虫库,aiohttp的使用
更多内容:https://aiohttp.readthedocs.io/en/stable/client_quickstart.html#make-a-request

"""

import asyncio
import aiohttp
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


async def asyfun(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as resp:
            if resp.status != 200:
                print(url)
                return 0
            return await resp.text()


start = time.time()
loop = asyncio.get_event_loop()

tasks = [asyncio.ensure_future(asyfun(i)) for i in url]

loop.run_until_complete(asyncio.wait(tasks))

print(tasks[3].result())

print(time.time() - start)
