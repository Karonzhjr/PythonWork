import requests

url = "https://timgsa.baidu.com/timg?image&quality=80" \
      "&size=b9999_10000&sec=1557655818702&di=826406e" \
      "265f31966f487464324ef5d3f&imgtype=0&src=http%" \
      "3A%2F%2Fpic1.win4000.com%2Fwallpaper%2F5%2F58a" \
      "7ecee20a0d.jpg"


result = requests.get(url, stream=True).raw.read()

with open("文艺唯美.jpg", "wb") as image:

    image.write(result)