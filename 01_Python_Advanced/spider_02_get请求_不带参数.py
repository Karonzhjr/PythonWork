import requests

# 1. 测试get请求的网站
result = requests.get("http://httpbin.org/get")

# 2. 获取返回值里面的源代码
print(result.text)

"""
运行结果：

请求头文件
{
  "args": {}, 
  "headers": {
    "Accept": "*/*", 
    "Accept-Encoding": "gzip, deflate", 
    "Host": "httpbin.org", 
    "User-Agent": "python-requests/2.21.0"
  }, 
  "origin": "223.87.250.114, 223.87.250.114", 
  "url": "https://httpbin.org/get"
}

重要的是：1、"Host"——服务器地址
        2、"User-Agent"——请求者的身份信息
"""