print("输入网页A")
print("向服务器发送请求")
print("等待服务器响应")
print("得到响应信息A1")

print("输入网页B")
print("向服务器发送请求")
print("等待服务器响应")
print("得到响应信息B1")

print("输入网页C")
print("向服务器发送请求")
print("等待服务器响应")
print("得到响应信息C1")

...


def fun(a):
    print(f"输入网页{a}")
    print("向服务器发送请求")
    print("等待服务器响应")
    print(f"得到响应信息{a}1")

fun('A')
fun('B')
fun('C')
