"""
往期爬虫内容回顾
0.  python 基本语法,语句:for循环语句
    list,列表的创建
    list,列表的索引
    list,列表的切片操作
1.  导入 requests 请求库
1.1 什么是requests headers(请求访问网页时,携带的额外信息<本文代码中的headers仅表示模拟的浏览器信息>)
2.  导入 PyQuery html解析库
2.1 <div class='items' id='itemsid'>测试文本</div>,
    理解此html代码中,什么是标签,什么属性
    CSS选择器,是PyQuery对html元素进行选择的方法
    标签名可以直接写
    id属性值,用#表示
    class属性值,用.表示
    更多了解学习:http://www.bejson.com/apidoc/jquery/next_1.html
2.2 PyQuery库,pq(html).find(CSS选择器).items()方法可以获取到多个对象
2.3 PyQuery库,pq(html).find(CSS选择器).text()方法可以获取到对象的文本信息
2.4 PyQuery库,pq(html).find(CSS选择器).attr('属性名')方法可以获取到标签中属性值
    更多内容:https://pythonhosted.org/pyquery/#
A
"""

import requests
from pyquery import PyQuery as pq



# requests 请求头
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36"
}




url = "http://maoyan.com/films"

respones = requests.get(url, headers=headers)





html=respones.text
doc = pq(html)




a = doc('#movie-item')





.items()

for i in a:
    print(i.text())
