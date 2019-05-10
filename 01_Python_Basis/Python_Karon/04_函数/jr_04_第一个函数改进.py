# 使用单步调试查看程序执行的步骤

name = "小明"

# 1. 定义好函数


def say_hello():
    """打招呼"""

    print("hello Karon")
    print("hello world")
    print("hello Python")


print(name)

# 2. 调用函数
say_hello()  # 在此处 Ctrl + Q 查看函数文档字符串

print(name)