# 1. 提示用户输入苹果的单价
price = float(input("苹果的单价："))  # 如果用户输入的不是一个数字，而是其他字符，程序执行时会出错，该如何处理呢？

# 2. 提示用户输入苹果的重量
weight = float(input("苹果的重量："))

# 3. 计算金额
money = price * weight

print(money)