"""
打印一下图形在输出上面（4×5）
* * * * *
*       *
*       *
* * * * *

思路：
    1. 正常利用for循环控制打印行；
    2. 如果是第一行和最后一行，则完整打印；
    3. 否则，判断打印列，如果是第一列或者最后一列，则打印星号，否则打印空格。
"""
for i in range(4):
    if i == 0 or i == 3:
        print("* " * 5)

    if i == 1 or i == 2:
        for j in range(5):
            if j == 0 or j == 4:
                print("* ", end="")
            else:
                print("  ", end="")
        print()
print("=========")
"""
打印实心三角
*
* *
* * *
* * * *
* * * * *
"""

for i in range(5):
    for j in range(i+1):
        print("* ", end = "")
    print()
print("=========")
"""
打印空心三角形（5×5）
*
* *
*   *
*     *
* * * * *
"""
for i in range(5):
    for j in range(i+1):
        if i == 4:
            print("* ", end="")
            continue
        if j == 0 or j == i:
            print("* ", end="")
        else:
            print("  ", end="")
    print()
print("=========")
"""
打印倒立三角
* * * * * 
* * * * 
* * * 
* * 
* 
i-for控制行号
j-for控制列号
"""
for i in range(5):
    for j in range(5-i):
        print("* ", end="")
    print()

