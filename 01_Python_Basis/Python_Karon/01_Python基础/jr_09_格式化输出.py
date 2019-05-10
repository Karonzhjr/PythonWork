# 定义一个字符串变量name，输出 我的名字是 小明，请多多关照！
name = '小明'
print('我的名字是 %s，请多多关照！' % name)

# 定义一个整数变量stu_num，输出 我的学号是 000001，请多多关照！
stu_num = 1
print('我的学号是 %06d，请多多关照！' % stu_num)  # %06d 表示 不足6位时用0补足，超过6位完整显示

# 定义小数 price、weight、money
# 输出 苹果单价 9.00 元/斤，购买了 5.00 斤，需要支付 45.00 斤
price = 9.68
weight = 5.66
money = price * weight

print('苹果单价 %.2f 元/斤，购买了 %.3f 斤，需要支付 %.4f 斤' % (price, weight, money))

# 定义一个小数 scale，输出 数据比例是 10.00%
scale = 0.25 * 10
print('数据比例是 %.2f%%' % scale)

scale = 0.25
print('数据比例是 %.2f%%' % scale * 10)

scale = 0.25
print('数据比例是 %.2f%%' % (scale * 10))

int = 100.3
print(int)