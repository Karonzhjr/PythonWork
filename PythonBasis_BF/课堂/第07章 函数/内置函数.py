"""
常用内置函数(9个)
    abs(), sum(), sorted(list, key), list.sort(), isinstance(), pow(), round(), eval(), exec()
"""
# abs() 求绝对值
print(abs(-100))
L = [-10, -888, 999, -6666]
print(list(map(lambda i: abs(i), L)))

# eval() 执行字符串类型的运算
print(eval("1+8*2"))

# exec() 执行字符串包含的Python语句
c = """
a = 10
b = 20
print(a+b)
"""
exec(c)