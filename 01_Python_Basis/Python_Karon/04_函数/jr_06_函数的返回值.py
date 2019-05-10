def sum_2_num(num1, num2):
    """对两个数字求和"""

    result = num1 + num2

    return result

    # return 之后的语句不会执行
    print("本行语句不会执行")


sum_result = sum_2_num(88, 66)

print("计算结果：%d" % sum_result)