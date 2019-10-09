"""
分享内容:
在开始介绍异步爬虫之前,我们先整理一下普通爬虫的基本流程
构建URL-->请求网页(得到响应信息)-->解析响应信息(得到我们感兴趣的内容)-->内容整理,格式化输出,保存到本地或数据库
"""

import time
import random


def req(URL):
    print(f"输入网页<{URL}>,请求网页")
    random.seed()
    t = random.randint(1, 4)
    time.sleep(t)
    print(f"{t}秒后,得到网页<{URL}>的响应信息")


"""
# 备注:
本节课内容主要讲异步爬虫内容,
在此其它方法先省略不写....
"""
a=time.time()
# 调用函数方法,对网页进行请求
for i in range(3):
    req(i)

print(time.time()-a)
