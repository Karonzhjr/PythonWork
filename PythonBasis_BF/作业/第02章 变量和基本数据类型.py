"""
1、上机题
    编写四个表达式，用于加减乘除的运算，动态接收用户输入的数据用于计算。
"""
num_1 = int(input("请输入一个数："))
num_2 = int(input("请输入另一个数："))

print("{0}+{1}={2}".format(num_1, num_2, num_1+num_2))  # 加法
print("{0}-{1}={2}".format(num_1, num_2, num_1-num_2))  # 减法
print("{0}*{1}={2}".format(num_1, num_2, num_1*num_2))  # 乘法
if num_2 != 0:
    print("{0}/{1}={2}".format(num_1, num_2, num_1 / num_2))  # 除法
else:
    num_2 = int(input("请重新输入一个不为零的除数："))
    print("{0}/{1}={2}".format(num_1, num_2, num_1 / num_2))  # 除法

"""
2、上机题
    声明一个列表存储一些信息，依次访问每个元素并且打印出来。
"""
lS = ['四川', '重庆', '北京', '成都', '未来人类', '外星人笔记本']

for _ in lS:
    print(_)

"""
3、上机题
    使用字典来存储一个学员信息，包括姓名，年龄，地址等等，将存储的学员信息打印出来。
"""
dictionary = {'姓名': '张三', '年龄': 18, '地址': '成都'}
for (i, j) in dictionary.items():
    print(i, j)