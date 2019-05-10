# 1.判断空白字符
space_str1 = "        "
space_str2 = "  \n\t\r"
space_str3 = "       a"

print(space_str1.isspace())
print(space_str2.isspace())
print(space_str3.isspace())

# 2. 判断字符串中是否只包含数字
num_str = "1"

print(num_str)
print(num_str.isdecimal())
print(num_str.isdigit())
print(num_str.isnumeric())