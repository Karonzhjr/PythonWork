"""
1、上机题
    创建一个字典保存学员信息，至少包含：姓名，年龄，性别，学号。
"""
dictInfo = {'姓名': '陈六', '年龄': 18, '性别': '男', '学号': 20190405}   # 创建一个字典保存学员信息
# for x, y in dictInfo.items():
#     print(x, y)  # 打印学员信息，检查是否保存正确

"""
2、上机题
    分别实现添加，删除和修改学员信息。
"""
dictInfo['班级'] = 17   # 添加
del dictInfo['性别']    # 删除
dictInfo['年龄'] = 19   # 修改

for x, y in dictInfo.items():
    print(x, y)  # 打印学员信息，检查是否修改成功

"""
3、上机题
    用字典模拟出现实生活中的字典，存储词汇和词汇的含义。
"""
dictWord = {'apparent': '显然的，明白的', 'indifferent': '不关心的', 'pregnant': '怀孕的，充满的', 'initial': '第一的，开始的'}
for i, j in dictWord.items():
    print(i, j)  # 打印已存储的字典

"""
4、上机题
    实现该字典的动态添加，添加的数据来源为用户动态输入。
"""

while True:
    i = input("请输入单词：")
    j = input("请输入单词的含义：")
    dictWord[i] = j  # 添加新单词及其含义
    print(dictWord)  # 打印出所有字典