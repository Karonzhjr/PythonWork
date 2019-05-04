"""
1、上机题
    定义一个函数，实现两个数四则运算，要注意有3个参数，分别是运算符和两个用于运算的数字。
"""
def FourAri(num1, operator, num2):
    if operator == '+':
        result = num1 + num2    # 加法
    elif operator == '-':
        result = num1 - num2    # 减法
    elif operator == '*':
        result = num1 * num2    # 乘法
    elif operator == '/':
        if num2 != 0:
            result = num1 / num2 # 除法
        else:
            result = "做除法，要求除数不能为零！"

    return result


while True:
    first_num = input("请输入一个数：")
    operator = input("请输入运算符（+、-、*、/）：")
    second_num = input("请输入另一个数：")

    if first_num.isdigit() and second_num.isdigit():
        first_num = int(first_num)
        second_num = int(second_num)
        print(FourAri(first_num, operator, second_num))


