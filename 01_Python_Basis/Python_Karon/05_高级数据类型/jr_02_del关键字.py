name_list = ["zhangsan", "lisi", "wangwu"]

# 使用 del 关键字删除列表元素，del 从内存中删除变量，后续代码将不能使用该变量
# 在日常开发中，建议使用列表提供的方法 pop、remove 来删除列表中的元素
del name_list[1]

print(name_list)