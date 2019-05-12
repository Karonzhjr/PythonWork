import requests

url = "http://github.com/timeline.json"

result = requests.get(url)

print(type(result.text))  # <class 'str'>
print(result.text)

print("-" * 26)
print("get请求，解析json数据")
print("-" * 26)

print(type(result.json))  # <class 'method'>
print(result.json)

