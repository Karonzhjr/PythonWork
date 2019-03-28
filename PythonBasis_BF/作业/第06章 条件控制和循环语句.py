"""
1、利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示。
"""
# score = 58
# if score >= 90:
#     print("A")
# elif 60 < score <= 89:
#     print("B")
# else:
#     print("C")

"""
2、猜拳游戏：random.randint(x,y)返x到y之的随机数
"""
# import random
# fingerPlay = ['石头', '剪刀', '布']
# computer = random.randint(0, 2)  # 电脑随机出拳
# user = int(input("请出拳（输入0,1,2三个数字中的一个）："))  # 玩家出拳
# if computer - user == -1 or computer - user == -2:
#     print("电脑获胜！")
# elif computer - user == 0:
#     print("平局！")
# else:
#     print("玩家获胜！")

"""
3、打印9*9乘法表
"""
# for i in range(1, 10):
#     for j in range(1, i+1): # 注意此处是i+1
#         print("%d * %d = %2d"%(i, j, i*j), end = "  ")
#     print()

"""
4、3000米长的绳子，每天减一半。问多少天这个绳子会小于5米？
"""
# length = 3000
# countDays = 0
# while length >= 5:
#     countDays += 1
#     length /= 2

# print("3000米长的绳子，每天减一半。%d天这个绳子会小于5米。"%countDays)

"""
5、计算从1到某个值以内所有能被3或者17整除的数的和并输出.
"""
# userNum = int(input("请输入一个大于1的正整数："))
# total = 0
# for i in range(1, userNum):
#     if i%3 ==0 or i%17 == 0:
#         total += i
#
# print("从1到%d以内所有能被3或者17整除的数的和：%d"%(userNum, total))

"""
6、随意输入一个整数，判断是否是素数（质数）。
质数又称素数，一个大于1的自然数，除了1和它自身外，不能被其他自然数整除的数叫做质数；否则称为合数。
注意：1既不是素数也不是合数。
"""
# primeNum = int(input("请输入一个大于1的整数，判断是否是素数："))
# for i in range(2, primeNum):
#     if primeNum % i ==0:
#         print("{0}不是素数。".format(primeNum))
#         break
# else:
#     print("{0}是素数。".format(primeNum))

"""
7、创建一个名为favorite_places的字典。在这个字典中，将三个人的名字用作键；
对于其中的每个人，都存储他喜欢的1~3个地方（作为值），朋友指出他们喜欢的一个地方（input）。
遍历这个字典，并将其中每个人的名字及其喜欢的地方打印出来。
"""
# names = ['张三', '李四', '王五']
# places = [['成都', '杭州', '北京'], ['广州', '杭州', '北京'], ['成都', '天津', '重庆']]
# favorite_place = dict(zip(names, places))
# # 朋友输入一个地方，看看有哪些人喜欢
# friendPlace = input("请输入一个地方：")
# for i in favorite_place.keys():
#     if friendPlace in favorite_place[i]:
#         print("{0}喜欢{1}".format(i, friendPlace))

"""
8、用控制台程序倒着输出九九乘法表
"""
# for i in range(9, 0, -1):
#     for j in range(9, i-1, -1):
#         print("%d * %d = %2d"%(i, j, i*j), end="  ")
#     print()

"""
9、输出一个用*组成的矩形，如：
* * * * * * * * *
*               *
*               *
*               *
* * * * * * * * *
"""
# for i in range(0, 5): # i控制行
#     for j in range(0, 9): # j控制列
#         if 0<i<4 and 0<j<8:
#             print("  ", end="") # 打印空格
#         else:
#             print("* ", end="") # 打印*号
#     print()

"""
10、首先要求用户输入学生的数目放入到变量n中，如果这个数大于0，那么就循环n次接收n个学生的成绩，计算总分及平均分。
否则输出“学生的人数不能为负数”。
"""
# n = int(input("输入学生的数目："))
# studentMark = []  # 空列表，存储学生成绩

# if n > 0:
#     for i in range(0, n):
#         stuScore = int(input("接收学生的成绩："))
#         studentMark.append(stuScore)
# else:
#     print("学生的人数不能为负数!")
#
# print("学生成绩总分：{0}，平均分：{1}".format(sum(studentMark), sum(studentMark)/len(studentMark)))

"""
11、循环问“老婆，你爱我吗？”，如果回答的是“爱”，那么就结束循环，否则就继续问。用程序描述这个故事.
"""
# while True:
#     print("老婆，你爱我吗？")
#     answerDarling = input("老婆回答（爱 或者 不爱）：")
#     if answerDarling == "爱":
#         print("宝贝，我也爱你💖💖💖")
#         break
#     else:
#         continue

"""
12、L=[75，98，59，81，66，43，69，85]
    现在老师只想统计及格分数的平均分，就要把x<60的分数剔除掉
"""
# L = [75, 98, 59, 81, 66, 43, 69, 85]  # 学生成绩
# passingScore = []  # 空列表，存储及格分数
#
# for i in range(len(L)):
#     if L[i] > 60:
#         passingScore.append(L[i])
#
# print("及格分数的平均分：%d" % sum(passingScore))

"""
13、0-100的while循环进行改造，通过增加continue语句，使得只计算奇数的和
"""
# i = 0
# total = 0
# while True:
#     i += 1
#     if i > 100:
#         break
#     elif i % 2 == 0:
#         continue
#     total += i
# print("0-100所有奇数和为：%d" % total)

"""
14、利用while True无限循环配合break语句，计算1+2+4+8+16+.…的前20项的和
"""
# i = 1
# j = 1  # 项
# total = 0
#
# while True:
#     total += i
#     i *= 2
#     j += 1
#     if j > 20:
#         break
# print("1+2+4+8+16+.…的前20项的和：%d" % total)

"""
15、names = ['Tom', 'Billy', 'Jefferson', 'Andrew', 'Wesley', 'Steven', 'Joe', 'Alice', 'Jill', 'Ana', 'Wendy', 'Jennifer', 'Sherry', 'Eva']
找出上述名字中长度大于4的名字组成列表打印出来.
过滤掉长度小于5的字符串列表，并将剩下的转换成大写字母.
"""
# names = ['Tom', 'Billy', 'Jefferson', 'Andrew', 'Wesley', 'Steven', 'Joe', 'Alice', 'Jill', 'Ana', 'Wendy', 'Jennifer', 'Sherry', 'Eva']
# NAMES = []
# for i in names:
#     if len(i) > 4:
#         NAMES.append(i)
#     if len(i) >= 5:
#         print(i.upper())
# print(NAMES)

"""
16、对列表中为偶数的元素进行立方运算a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
"""
# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for i in a:
#     if i%2 == 0:
#         print(pow(i, 3))

"""
17、打印出所有的“水仙花数”，所谓“水仙花数”是指一个三位数，其各位数字立方和等于该数本身。
    例如：153是一个“水仙花数”，因为153=1的三次方+5的三次方+3的三次方。
    程序分析：利用for循环控制100-999个数，每个数分解出个位，十位，百位。
"""
# for i in range(100, 1000):
#     # (i//100) 百位
#     # ((i-(i//100)*100)//10) 十位
#     # (((i-(i//100)*100)-(((i-(i//100)*100)//10))*10)) 个位
#     if i == (i//100)**3 + ((i-(i//100)*100)//10)**3 + (((i-(i//100)*100)-(((i-(i//100)*100)//10))*10))**3:
#         print("%d是水仙花数" % i)

for i in range(100, 1000):
    # (i//100) 百位
    # (i//10)%10 十位
    # (i%10) 个位
    if i == (i//100)**3 + ((i//10)%10)**3 + (i%10)**3:
        print("%d是水仙花数" % i)

"""
18、打印出如下图案（菱形）
   *
  ***
 *****
*******
 *****
  ***
   *
"""
# for i in range(4):  # 控制行
#     for j in range(4-i):    # 打印空格
#         print(" ", end="")
#     for k in range(2*i+1):  # 打印*号
#         print("*", end="")
#     print()
# for l in range(3, 0, -1):
#     for m in range(3-l+2, 0, -1):  # 打印空格
#         print(" ", end="")
#     for n in range(2*l-1, 0, -1):  # 打印*号
#         print("*", end="")
#     print()

"""

19、有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
    程序分析：可填在百位、十位、个位的数字都是1、2、3、4。
    组成所有的排列后再去掉不满足条件的排列。（用列表推导式）
"""
# 参考网络别人代码
# count = 0 # 统计个数
# for x in range(1, 5):
#     for y in range(1, 5):
#         for z in range(1, 5):
#             if x!=y and y!=z and z!=x:
#                 count += 1
#                 print("由1、2、3、4能组成的互不相同且无重复数字的三位数：%d%d%d"%(x, y, z))
# print()
# print("由1、2、3、4能组成%d个互不相同且无重复数字的三位数"%count)

"""
20、一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同。
"""
# for i in range(10000, 99999):
#     # i//10000       万位
#     # (i//1000)%10   千位
#     # (i//100)%10    百位
#     # (i//10)%10     十位
#     # (i%10)         个位
#     if i//10000 == (i%10) and (i//1000)%10 == (i//10)%10:
#         print("%d是回文数"%i)
