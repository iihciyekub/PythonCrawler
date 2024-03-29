"""
分享内容:
1.创建协程对象,调用协程(协程带返回值的情况)
2.创建多少协程对象,并执行
"""

import time
import random
import asyncio


# 定义一个协程方法
async def req(URL):
    print(f"输入网页<{URL}>,请求网页")
    random.seed()
    t = random.randint(1, 4)
    # await 表示挂起的意思
    await asyncio.sleep(t)
    print(f"{t}秒后,得到网页<{URL}>的响应信息")
    respone = f'{URL},的响应信息'
    return respone


# 返回一个协程对象,调用方法比较特殊
# await 表示挂起 异步执行其他内容


"""
# 备注:
本节课内容主要讲异步爬虫内容,
在此其它方法先省略不写....
"""
# 第一种方法:只有一个协程被调用时
start = time.time()
task = asyncio.ensure_future(req(1))
loop = asyncio.get_event_loop()
loop.run_until_complete(task)
print(task.result())
print(time.time() - start)

# 第2种方法:有多个协调要被调用时,将方法组合成list.通过asyncio.gather()方法组拼在一起
a = time.time()
ab = loop.create_task(req(1))
ab2 = asyncio.ensure_future(req(2))
tasks = [ab, ab2]
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.gather(*tasks))
for i in tasks:
    print(i.result())

print(time.time() - a)

# 第3种方法:生成数组.通过asyncio.gather()方法组拼在一起
a = time.time()
tasks = [asyncio.ensure_future(req(i)) for i in range(10)]
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))
for i in tasks:
    print(i.result())
loop.close()
print(time.time() - a)
