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