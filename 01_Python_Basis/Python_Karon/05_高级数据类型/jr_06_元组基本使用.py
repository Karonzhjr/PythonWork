info_tuple = ("张三", 18, 1.75)

# 1. 取值和取索引值
print(info_tuple[0])
print(info_tuple.index("张三"))  # 已经知道数据的内容，希望知道该数据在元组中的索引

# 2. 统计计数
print(info_tuple.count("张三"))

# 3. 统计元组中包含元素的个数
print(len(info_tuple))