# 1. 输入用户年龄
age = int(input('请输入年龄：'))

# 2. 判断是否满足18岁（>=）
if age >= 18:
    # 3. 如果满了18岁，可以进网吧嗨
    print("您已经成年，欢迎进入网吧")

else:
    # 4. 如果没有满18岁，提示回家写作业
    print('您还没有成年，回家写作业吧')

# 这句代码无论条件是否成立都会执行！
print('看看什么时候执行这句代码')