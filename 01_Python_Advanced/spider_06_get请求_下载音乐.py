import requests

"""
来源平台：千千音乐
平台网站：http://music.taihe.com/
"""

url = "http://zhangmenshiting.qianqian.com/data2/music/" \
      "24cb0403ff9cc29214c6f31aeb0b409e/596612844/596612844.mp3" \
      "?xcode=056a70a3dc08d9eb25903e2d9e216d08"

result = requests.get(url, stream=True).raw.read()

with open("只是没有如果.mp3", "wb") as music:

    music.write(result)

"""
运行结果：
    爬取成功，成功下载音乐
    只是没有如果.mp3
"""