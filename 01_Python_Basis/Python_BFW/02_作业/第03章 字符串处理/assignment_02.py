"""
2.上机题
（1）计算字符串中子串出现的次数.
（2）从键盘输入一个字符串，将小写字母全部转换成大写字母
（3）输入一个全部大写的字符串，转换成头部大写，后面小写
"""
if __name__ == '__main__':
    while True:
        some_string = input("请任意输入一个字符串：")
        sub_string = input("请输入字符串中的任意子串，返回该子串出现的次数：")

        print(some_string.count(sub_string))   # 计算字符串中子串出现的次数
        print(some_string.upper())  # 将小写字母全部转换成大写字母
        print(some_string.title())  # 转换成头部大写，后面小写