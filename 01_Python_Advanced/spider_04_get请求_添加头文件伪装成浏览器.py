import requests

result_1 = requests.get("https://www.zhihu.com")

print(result_1.status_code)

print("------不带头文件的get请求------")
print(result_1.text)


header = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) "
                        "AppleWebKit/537.36 (KHTML, like Gecko) "
                        "Chrome/72.0.3626.121 Safari/537.36"}
result_2 = requests.get("https://www.zhihu.com", headers = header)

print("------带头文件的get请求------")
print(result_2.text)