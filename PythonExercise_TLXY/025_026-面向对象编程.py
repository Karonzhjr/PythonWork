"""
1. 定义一个学生类
类属性：
    1.姓名
    2.年龄
    3.成绩（语文，数学，英语）每课成绩类型为整数
类方法：
    1.获取学生的姓名：get_name() 返回类型：str
    2.获取学生的年纪：get_age()返回类型：int
    3.返回3门科目中最高的分数，get_course()返回类型：int
"""

class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    def GetName(self):
        print(self.name)
        return None
    def GetAge(self):
        print(self.age)
        return None
    def GetScore(self):
        print(self.score)
        print("最高分：{0}".format(max(list(self.score.values()))))
        return None

zhjr = Student('春望', 29, {'语文': 96, '数学': 100, '英语': 98})
zhjr.GetName()
zhjr.GetAge()
zhjr.GetScore()
print('===========================')

"""
2. 定义一个字典类：DictClass，完成如下功能:
    (1).删除某个key del_dict(key)
    (2).判断某个键是否在字典里，如果在返回键对应的值，不在则返回‘not found' get_dict()
    (3).返回键组成的列表 返回类型：list get_key()
    (4).合并字典，并且返回合并后字典的values组成的列表，返回类型list update_dict()
"""
class DictClass(object):
    def __init__(self, dict1):
        self.dict1 = dict1

    def DelKey(self, key):
        if key in self.dict1.keys():
            del self.dict1[key]
            print(self.dict1)
            return '删除成功'
        else:
            return '{0}不在字典中'.format(key)

    def GetDict(self, key):
        if key in self.dict1.keys():
            return self.dict1[key]
        else:
            return '{0}不在字典中'.format(key)

    def GetKey(self):
        return list(self.dict1.keys())

    def UpdateDict(self, dict2):
        self.dict1 = dict(self.dict1, **dict2)
        return self.dict1

dict0 = DictClass({'语文': 96, '数学': 100, '英语': 98, '物理': 99})

print(dict0.DelKey('物理'))
print(dict0.GetDict('语文'))
print(dict0.GetKey())
print(dict0.UpdateDict({'历史':88, '地理': 89}))

"""
3. 定义一个列表的操作类 ListInfo
包括的方法:
    1.列表元素添加: add_key()
    2.列表元素取值: get_key()
    3.列表合并: update_list(list)
    4.删除并且返回最后一个元素: del_key()
"""
class ListInfo(object):
    def __init__(self, list1):
        self.list1 = list1

    def AddKey(self, key):
        self.list1.append(key)
        print(self.list1)
        return None

    def GetKey(self, num):
        print(self.list1[num])
        return None

    def UpdateList(self, list2):
        self.list1.extend(list2)
        print(self.list1)
        return None

    def DelList(self):
        print(self.list1.pop())
        return None

list0 = ListInfo([1, 2, 3, 4, 5, 6])

list0.AddKey(7)
list0.GetKey(0)
list0.UpdateList([666, 888, 999])
list0.DelList()

"""
4. 定义一个集合的操作类
包括的方法
    1.集合元素添加: add_setinfo()
    2.集合的交集: get_intersection()
    3.集合的并集: get_union()
    4.集合的差集: del_difference()
"""
class SetOp(object):
    def __init__(self, set1):
        self.set1 = set1

    def AddSet(self, element):
        self.set1.add(element)
        print(self.set1)
        return None
    def GetIntersection(self, set2):
        return self.set1.intersection(set2)
    def GetUnion(self, set2):
        return self.set1.union(set2)
    def GetDifference(self, set2):
        return self.set1.difference(set2)


setInfo = SetOp({11, 22, 33, 'Karon'})

setInfo.AddSet('Nina')
print(setInfo.GetIntersection({11, 88, 99, 33, 'Tina'}))
print(setInfo.GetUnion({11, 88, 99, 33, 'Tina'}))
print(setInfo.GetDifference({11, 88, 99, 33, 'Tina'}))
