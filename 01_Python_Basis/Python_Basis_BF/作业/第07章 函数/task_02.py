"""
2、上机题
    实现学生管理系统，使用自定义函数，完成对学员的增、删、改、查和退出学生管理系统
"""
def addname():
    nameinfo = input("请输入需要增加学员的姓名：")  # 输入学员姓名
    if nameinfo not in stuList:
        stuList.append(nameinfo)
        print("学员人数：{0}，现有学员名单：{1}".format(len(stuList), stuList))
    else:
        print("{0}学员已在名单中".format(nameinfo))


def delname():
    nameinfo = input('请输入需要删除学员的姓名：')
    stuList.remove(nameinfo)
    print("学员人数：{0}，现有学员名单：{1}".format(len(stuList), stuList))


def modify():
    nameinfo = input('请输入需要删除学员的姓名：')
    if nameinfo in stuList:
        pass


def quict():
    print('退出学生管理系统')


stuList = []   # 存储学员姓名

while True:
    flag = input('请输入您的操作（增、删、改、查和退出）：')
    if flag == '增':
        addname()
    elif flag == '删':
        delname()
    else:
        break



# nameinfo2 = input("请输入需要删除学员的姓名：")   # 输入学员姓名
# delname(nameinfo2)
