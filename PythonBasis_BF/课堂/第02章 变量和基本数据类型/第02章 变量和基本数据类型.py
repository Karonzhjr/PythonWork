"""
1.查看关键字的方法
"""
import keyword   # 引入关键字模块
print(keyword.kwlist)  # 打印全部关键字

"""
2.判断变量类型：(1)type(); (2)isinstance()
数字、字符串、元祖、列表、集合、字典
"""
numOne = 88
print(type(numOne))                # 输出结果：<class 'int'>
print(isinstance(numOne, int))     # 输出结果：True

numTwo = 99.99
print(type(numTwo))                # 输出结果：<class 'float'>
print(isinstance(numTwo, float))   # 输出结果：True

numThree = True
print(type(numThree))              # 输出结果：<class 'bool'>
print(isinstance(numThree, bool))  # 输出结果：True

numFour = False
print(type(numFour))               # 输出结果：<class 'bool'>
print(isinstance(numFour, bool))   # 输出结果：True

string = 'This is a man, Dan.'
print(type(string))                # 输出结果：<class 'str'>
print(isinstance(string, str))     # 输出结果：True

tup = (66, 88, 99)
print(type(tup))                   # 输出结果：<class 'tuple'>
print(isinstance(tup, tuple))      # 输出结果：True

lieBiao = [66, 88, 99]
print(type(lieBiao))               # 输出结果：<class 'list'>
print(isinstance(lieBiao, list))   # 输出结果：True

dictionary = {66: '六六大顺', '四季发财': 888, '九九为功': 9999}
print(type(dictionary))            # 输出结果：<class 'dict'>
print(isinstance(dictionary, dict))# 输出结果：True

jiHe = {66, 88, 99}
print(type(jiHe))                  # 输出结果：<class 'set'>
print(isinstance(jiHe, set))       # 输出结果：True

"""
3.操作字符串
"""
string1 = 'Good afternoon, '
string2 = 'Karon'
print(string1 + string2)  # 输出结果：Good afternoon, Karon
print(string1[5:14])      # 输出结果：afternoon

print(id(string))         # 原字符串地址，输出结果：2512537694472
print(id(string1[5:14]))  # 部分切片地址，输出结果：2512546612144
print(id(string1[:]))     # 完整切片地址，输出结果：2512537697784

print("string3=\'Hello, Python\'")  # 比较字符串前加r的区别
print(r"string3=\'Hello, Python\'")

"""
3.功能：有一个列表a[ ]，里面有若干个整数未知。我希望将里面的整数两两做差
（即a[1]-a[0],a[3]-a[2]....），并将得数保存在另一个列表b[ ]中，请问如何实现？
"""
