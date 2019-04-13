# 课堂练习
names = ['tom', 'jerry', 'anni']
ages = [19, 20, 17]
sexs = ['男', '女', '男']

from functools import reduce

# 格式化用户的英文名，要求首字母大写，其他字母小写
print(list(map(lambda x: x.capitalize(), names)))

# 合并数据：将用户英文名、年龄、性别三个集合的数据结合到一起，形成一个
allUser = list(map(lambda x,y,z: {'name': x, 'age': y, 'sex': z}, names, ages, sexs))
print(allUser)

# 过滤性别为男的用户
maleInfo = list(filter(lambda i: i['sex']=='男', allUser))
print(maleInfo)

# 求性别为男的用户的平均年龄
avgAge = reduce(lambda x,y: (x['age']+y['age'])/len(maleInfo), maleInfo)
print(avgAge)