"""
1、斐波那契数列
    1,1,2,3,5,8......
    F(1)=1,F(2)=1,F(n)=F(n-1)+F(n-2) (n>=2,n为正自然数)
"""
# def fibo(n):
#     if n == 1:
#         return 1
#     elif n == 2:
#         return 1
#     else:
#         return fibo(n-1)+fibo(n-2)
#
# print(fibo(10))
# print([fibo(i) for i in range(1, 11)])

"""
2、
    names = ['tom', 'jerry', 'anni']
    ages = [19, 20, 17]
    sexs = ['男', '女', '男']
    格式化用户的英文名，要求首字母大写，其他字母小写
    合并数据：将用户英文名、年龄、性别三个集合的数据结合到一起，形成一个
    过滤性别为男的用户
    求性别为男的用户的平均年龄
"""
# names = ['tom', 'jerry', 'anni']
# ages = [19, 20, 17]
# sexs = ['男', '女', '男']
#
# from functools import reduce
#
# # 格式化用户的英文名，要求首字母大写，其他字母小写
# print(list(map(lambda x: x.capitalize(), names)))
#
# # 合并数据：将用户英文名、年龄、性别三个集合的数据结合到一起，形成一个
# allUser = list(map(lambda x,y,z: {'name': x, 'age': y, 'sex': z}, names, ages, sexs))
# print(allUser)
#
# # 过滤性别为男的用户
# maleInfo = list(filter(lambda i: i['sex']=='男', allUser))
# print(maleInfo)
#
# # 求性别为男的用户的平均年龄
# avgAge = reduce(lambda x,y: (x['age']+y['age'])/len(maleInfo), maleInfo)
# print(avgAge)

"""
3、定义一个函数，实现两个数四则运算，要注意有3个参数，分别是运算符和两个用于运算的数字。
   两个数字和运算符需要接收用户输入的值.
"""
def computer(i, j, k):

    return eval("'i'+'j'+'k'")

i = int(input("请输入一个数字："))
j = input("请输入一个运算符（+，-，*，/）：")
k = int(input("请输入一个数字："))
print(computer(i, j, k))