import requests

user_params = {"name": "Karon",
               "age": 30}

result = requests.get("http://httpbin.org/get", params=user_params)

"""

实际中更多使用：
result = requests.get("http://httpbin.org/get?name=Karon&age=30")

"""

print(result.status_code)

print(result.text)

"""
运行结果：

{
  "args": {
    "age": "30", 
    "name": "Karon"
  }, 
  "headers": {
    "Accept": "*/*", 
    "Accept-Encoding": "gzip, deflate", 
    "Host": "httpbin.org", 
    "User-Agent": "python-requests/2.21.0"
  }, 
  "origin": "223.87.250.114, 223.87.250.114", 
  "url": "https://httpbin.org/get?name=Karon&age=30"
}

"""