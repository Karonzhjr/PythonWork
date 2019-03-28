# """
# 作业01：
# 创建一个名为favorite_places的字典。
# 在这个字典中，将三个人的名字用作键；对于其中的每个人，都存储他喜欢的1~3个地方。
# """
# name=['张三','李四','王五']
# places=[['成都','重庆','北京'],['上海','南京','杭州'],['广州','天津','纽约']]
# print(dict(zip(name,places)))
#
# """
# 作业02：
# 创建多个字典，对于每个字典，都使用一个宠物的名称来给它命名；
# 在每个字典中，包含宠物的类型及其主人的名字。
# 将这些字典存储在一个名为pets的列表中，再遍历该列表，并将宠物的所有信息都打印出来。
# """
# dict_tiaotiao={'比熊':'Nina'}
# dict_pangpang={'哈士奇':'张三'}
# dict_nini={'吉娃娃':'李四'}
# pets=[dict_tiaotiao,dict_pangpang,dict_nini]
# for i in pets:
#     print(i)
#
# """
# 作业03：
# 分别创建一个列表，元组，集合，字典，进行增删改查操作？
# """
# listOne=['A','B','C']
# tupleTwo=(1,2,3)
# setThree={'张三','李四','王五'}
# dictFour={'桌子':'板凳','电脑':'鼠标','杯子':'吸管'}
# #列表增删改查操作
# listOne.append('D') #曾
# del listOne[0] #删
# listOne[1]='E' #改
# print(listOne[2]) #查
# print(listOne)
#
# #元组增删改查操作
# tupleList = list(tupleTwo) #将元组转换为列表
# tupleList.append(666) #增加
# tupleList[1]=888 #改
# print(tupleTwo[0]) #查询
# tupleTwo=tuple(tupleList) #将列表转换为元组
# print(tupleTwo)
# del tupleTwo #删除
#
# #集合增删改查操作
# setThree.add('陈六') #增加
# setList=list(setThree)
# setList[1]='言几又'#改
# setThree=set(setList)
# print(setThree)
# print(list(setThree)[0]) #查
# setThree.clear() #删除
#
# #字典增删改查操作
# dictFour['老师']='学生' #增加
# dictFour['电脑']='无线鼠标' #改
# print(dictFour['桌子']) #查
# print(dictFour)
# del dictFour #删
#
# """
# 作业04：
# 编写四个表达式，用于加减乘除的运算，动态接收用户输入的数据用于计算.
# """
# num1 = int(input("请输入一个数字："))
# num2 = int(input("请再输入一个数字："))
#
# print("{0}+{1}={2}".format(num1, num2, num1+num2))
# print("{0}-{1}={2}".format(num1, num2, num1-num2))
# print("{0}*{1}={2}".format(num1, num2, num1*num2))
#
# if num2==0:
#     num2 = int(input("除数不能等于0，请重新输入一个不等于0的数字："))
#     print("{0}/{1}={2}".format(num1, num2, num1/num2))
# else:
#     print("{0}/{1}={2}".format(num1, num2, num1/num2))


# """
# 作业05：
# 声明一个列表存储一些信息，依次访问每个元素并且打印出来.
# """
# listPra=['武侯区','天府新区','龙泉驿区','金牛区']
# for i in listPra:
#     print(i)

"""
作业06：
使用字典来存储一个学员的信息，包括姓名，年龄，地址等等，
将存储的学员的信息打印出来
"""
# dictInfo={'张三':{'年龄':18, '地址':'成都'}, '李四':{'年龄':28, '地址':'重庆'}, '王五':{'年龄':38, '地址':'北京'}}
# print(list(dictInfo.items()))

# dictInfo1=['张三', '李四', '王五']
# dictInfo2=[{'年龄':18, '地址':'成都'}, {'年龄':28, '地址':'重庆'}, {'年龄':38, '地址':'北京'}]
# dictInfo=dict(zip(dictInfo1,dictInfo2))
# for i,j in dictInfo.items():
#     print(i,j)

"""
从键盘输入一个字符串，将小写字母全部转换成大写字母，将字符串以列表的形式输出（如果字符串包含整数，并取整）？
"""
# string = input("请输入一个字符串：")
# listStr=[]
# for i in string:
#     if i.isdigit():
#         listStr.append(i)
#     else:
#         listStr.append(i.upper())
# print(listStr)

"""
随机输入8位以内的的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。
"""
# num = input("请随机输入一个8位以内的的正整数：")
# listNum=list(num)
# listNum.reverse() #逆序
# print("您输入的是一个{0}位数".format(len(listNum)))
# print(listNum) #逆序打印

"""
作业09：
一球从n米（自己输入）高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？
"""


# hig=int(input("请输入高度："))
# totalM=0
# for i in range(10):
#     totalM += hig
#     hig /= 2
# print("在第10次落地时，共经过{0}米，第10次反弹{1}高".format(totalM, hig))


"""
作业10：
输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数
"""
# string=input("请输入一个字符串：")
# numAl=0
# numSp=0
# numDi=0
# numOt=0
# for i in string:
#     if i.isalpha():
#         numAl+=1
#     elif i.isspace():
#         numSp+=1
#     elif i.isdigit():
#         numDi+=1
#     else:
#         numOt+=1
# print("英文字母有{0}个，空格有{1}个，数字有{2}个，其他字符有{3}。".format(numAl, numSp, numDi, numOt))