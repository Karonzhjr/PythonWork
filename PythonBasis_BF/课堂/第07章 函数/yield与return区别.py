def GetNum(n):
    i = 0
    while i <= n:
        # print(i)
        # return i
        yield i
        i+=1

# GetNum(8)
# print(GetNum(8))
a = GetNum(8)
# print(next(a))
# print(next(a))
for i in a:
    print(i)