"""
姓名：小明
年龄：18
性别：是男生
身高：1.75米
体重：75.0公斤

利用”单步调试“确认变量中保存数据的类型
"""

# 在Python中定义变量时，不需要指定变量的类型
# 在运行的时候，Python解释器会根据赋值语句等号右侧的数据自动推导出变量中保存数据的准确类型
name = '小明'  # str 表示时一个字符串类型
age = 18  # int 表示是一个整数类型
gender = True  # bool 表示是一个布尔类型，真 True 或 假 False
height = 1.75  # float 表示是一个小数类型，浮点数
weight = 75.0

print(name)