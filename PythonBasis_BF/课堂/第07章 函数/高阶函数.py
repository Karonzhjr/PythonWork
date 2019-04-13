"""
常用高阶函数(3个)
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

