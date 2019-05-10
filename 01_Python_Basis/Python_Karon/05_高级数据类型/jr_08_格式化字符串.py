info_tuple = ("小明", 18, 1.75)

# 格式化字符串后面的（）本质上就是元组
print("%s 年龄是 %d 身高是 %.2f" % info_tuple)

info_str = "%s 年龄是 %d 身高是 %.2f" % info_tuple  # 元组拼接字符串 生成 一个新的字符串

print(info_str)