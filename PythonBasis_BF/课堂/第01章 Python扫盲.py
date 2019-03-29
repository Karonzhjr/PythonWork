"""
第一个程序
"""
print("Hello Python!")

# print absolute value of an integer
a = 100
if a >= 0:
    print(a)
else:
    print(-a)

"""
功能：输出自己的姓名和年龄
要求：使用变量接收用户输入的姓名和年龄，然后输出
"""
name = input("请输入您的姓名：")
age = input("请输入您的年龄：")
print("您的姓名是：" + name + "，" + "您的年龄是：" + age)