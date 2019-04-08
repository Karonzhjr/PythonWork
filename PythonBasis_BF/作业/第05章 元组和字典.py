"""
1、上机题
    创建一个字典保存学员信息，至少包含：姓名，年龄，性别，学号。
"""
dictInfo = {'姓名': '陈六', '年龄': 18, '性别': '男', '学号': 20190405}   # 创建一个字典保存学员信息
for x, y in dictInfo.items():
    print(x, y)

"""
2、上机题
    分别实现添加，删除和修改学员信息。
"""
dictInfo['班级'] = 17   # 添加
del dictInfo['性别']    # 删除
dictInfo['年龄'] = 19   # 修改

for x, y in dictInfo.items():
    print(x, y)

"""
3、上机题
    用字典模拟出现实生活中的字典，存储词汇和词汇的含义。
"""
dictWord = {'happy': '高兴的', 'indifferent': '不关心的', 'computer': '电脑'}
for i, j in dictWord.items():
    print(i, j)

"""
4、上机题
    实现该字典的动态添加，添加的数据来源为用户动态输入。
"""
i = input("请输入键：")
j = input("请输入值：")
dictWord[i] = j
print(dictWord)
