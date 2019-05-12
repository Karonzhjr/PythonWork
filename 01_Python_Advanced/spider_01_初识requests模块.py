import requests

result = requests.get("http://www.ibeifeng.com/")

print(type(result))

print(result.status_code)

print(result.encoding)

print(result.cookies)

print(result.text)
print(result.content)
print(result.content.decode("gbk"))

