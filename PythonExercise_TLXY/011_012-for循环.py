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


