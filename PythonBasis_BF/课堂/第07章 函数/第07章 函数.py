"""
1、for循环实现求一个数的阶乘
"""

# 面向过程编程
total = 1
n = 10
for i in range(1, n+1):
    total *= i
print(total)

# 函数式编程
def factorial1(n):
    total = 1
    for i in range(1, n+1):
        total *= i
    print(total)

factorial1(10)

# 递归函数
def factorial2(n):
    if n == 1:
        return 1
    else:
        return n*factorial2(n-1)

print(factorial2(10))

"""
2、for循环和sum()实现求多维列表的和
   for循环和sum()结合求二维列表
"""
list2D = [1, 2, 3, [10, 20, 30], 4, 5, 6, [40, 50, 60]]

# 面向过程式编程
totallist1 = 0
for i in list2D:
    if isinstance(i, list):
        totallist1 += sum(i)
    else:
        totallist1 += i
print(totallist1)

# 函数式编程
from functools import reduce
def SumList(l):
    totallist2 = 0
    for j in l:
        if isinstance(j, list):
            # totallist2 += sum(j)
            totallist2 += reduce(lambda a,b: a+b, j)
        else:
            totallist2 += j
    return totallist2

print(SumList(list2D))

# 递归函数
def SumList(l):
    totallist2 = 0
    for j in l:
        if isinstance(j, list):
            totallist2 += SumList(j)
        else:
            totallist2 += j
    return totallist2

print(SumList(list2D))

"""
3、斐波那契数列
    1,1,2,3,5,8......
    F(1)=1,F(2)=1,F(n)=F(n-1)+F(n-2) (n>=2,n为正自然数)
"""
def fibo(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)

print(fibo(10))
print([fibo(i) for i in range(1, 11)])

"""
4、常用内置函数(9个)
abs(), sum(), sorted(list, key), list.sort(), isinstance(), pow(), round(), eval(), exec()
"""
# abs() 求绝对值
print(abs(-100))
L = [-10, -888, 999, -6666]
print(list(map(lambda i: abs(i), L)))

# eval() 执行字符串类型的运算
print(eval("1+8*2"))

# exec() 执行字符串包含的Python语句
c = """
a = 10
b = 20
print(a+b)
"""
exec(c)

"""
5、常用高阶函数(3个)
map(), filter(), reduce()
"""
# reduce() 应用
personInfo = [
    {'name': '张三', 'sex': 'male', 'age': 18},
    {'name': '李四', 'sex': 'female', 'age': 20},
    {'name': 'Anni', 'sex': 'female', 'age': 20},
    {'name': '王五', 'sex': 'male', 'age': 19}
]

"""
分成两组
{
    'male':[
        {'name':'张三', 'sex':'male', 'age':18},
        {'name':'王五', 'sex':'male', 'age':19}
    ],
    'femal':[
        {'name':'李四', 'sex':'female', 'age':20}, 
        {'name':'Anni', 'sex':'female', 'age':20}
    ]
}
"""
from functools import reduce
def GroupSex(x, y): # 传入personInfo的元素中的键值对
    """
    按照性别分组
    :param x: {'male':[],'female':[]}
    :param y: person_info 里面的元素（字典）
    :return:
    """
    if y['sex'] == 'male':
        x['male'].append(y)
    else:
        x['female'].append(y)
    return x

print(reduce(GroupSex, personInfo, {'male': [], 'female': []}))

# 课堂练习
names = ['tom', 'jerry', 'anni']
ages = [19, 20, 17]
sexs = ['男', '女', '男']

from functools import reduce

# 格式化用户的英文名，要求首字母大写，其他字母小写
print(list(map(lambda x: x.capitalize(), names)))

# 合并数据：将用户英文名、年龄、性别三个集合的数据结合到一起，形成一个
allUser = list(map(lambda x,y,z: {'name': x, 'age': y, 'sex': z}, names, ages, sexs))
print(allUser)

# 过滤性别为男的用户
maleInfo = list(filter(lambda i: i['sex']=='男', allUser))
print(maleInfo)

# 求性别为男的用户的平均年龄
avgAge = reduce(lambda x,y: (x['age']+y['age'])/len(maleInfo), maleInfo)
print(avgAge)
