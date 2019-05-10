hello_str = "hello hello"

# 1. 统计字符串长度
print(len(hello_str))

# 2. 统计某一小（子）字符串出现的次数
print(hello_str.count("llo"))
print(hello_str.count("lla"))

# 3. 某一个子字符串出现的位置，如果字符串不存在会报错
print(hello_str.index("llo"))
