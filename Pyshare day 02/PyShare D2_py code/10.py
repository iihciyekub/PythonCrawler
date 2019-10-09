import requests
from pyquery import PyQuery as qp


response = requests.get('https://www.baidu.com/')
# 判断响应代码 200表示正常
print(response.status_code)
# 打印响应信息
print(response.text)
