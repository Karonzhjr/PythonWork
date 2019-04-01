"""
1、上机题
    创建一个列表，用于存储同学姓名，依次访问该列表中的每个元素，并且将每个同学的姓名打印出来
"""
nameList = ['张三', '李四', '王五', 'Dan', 'Tina', 'Ben']
for i in nameList:
    print(i)

"""
2、上机题
    在上一题的基础上，在打印同学姓名的基础上，加上一句问候语。
"""
nameList = ['张三', '李四', '王五', 'Dan', 'Tina', 'Ben']
for i in nameList:
    print("{0}同学，早上好，祝学业有成！".format(i))

"""
3、上机题
    将老师的姓名添加到列表末尾，将班主任的姓名添加到列表的开头
"""
nameList = ['李双红', '张三', '李四', '王五', 'Dan', 'Tina', 'Ben', '庄老师']
for i in nameList:
    if i == '李双红' or i == '庄老师':
        print("{0}老师，早上好，祝桃李满天下！".format(i))
    else:
        print("{0}同学，早上好，祝学业有成！".format(i))

"""
4、上机题
    缩减名单，并且打印出被删除的同学姓名，并且加上一句致歉的语句。
"""
nameList = ['李双红', '张三', '李四', '王五', 'Dan', 'Tina', 'Ben', '庄老师']
for i in nameList:
    if i == '李双红' or i == '庄老师':
        continue
    else:
        print(nameList.pop())