"""
1.上机题
分别使用加法、减法、乘法和除法编写四个表达式，使用print语句输出结果
要求：使用变量接收输入的数字用于计算
"""
if __name__ == '__main__':
    while True:
        num1 = input("请输入一个数：")
        num2 = input("请输入再一个数：")

        if num1.isdigit() and num2.isdigit():
            num1 = int(num1)
            num2 = int(num2)
            print("{0} + {1} = {2}".format(num1, num2, num1 + num2))  # 两数相加，并输出结果
            print("{0} - {1} = {2}".format(num1, num2, num1 - num2))  # 两数相减，并输出结果
            print("{0} * {1} = {2}".format(num1, num2, num1 * num2))  # 两数相乘，并输出结果

            while num2 == 0:  # 判断除数是否为零
                num2 = int(input("请重新输入一个不为0的除数："))  # 两数相除，并输出结果

            print("{0} / {1} = {2}".format(num1, num2, num1 / num2))
        else:
            print("请输入数字！")