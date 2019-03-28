"""
功能：判断年份是否为闰年
"""
while True:
    year = input("请输入年份：")

    if year.isdigit():
        year = int(year)
        if year % 4 == 0:
            print(str(year) + "是闰年")  # 或者这样写：print("{0}是闰年".format(year))
        else:
            print(str(year) + "不是闰年")
    else:
        print("傻帽，叫你输入年份，看不懂么？")