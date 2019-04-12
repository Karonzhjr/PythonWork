import time  # 导入时间模块

print(time.time())              # 查看当前时间戳

print(time.ctime())             # 查看当前可读性形式的时间字符串
print(time.ctime(time.time()))  # 查看当前可读性形式的时间字符串

print(time.localtime())         # 查看当前时间元组


"""
练习1：
    时间戳 > 时间元祖 > 时间字符串
"""
times = time.time()  # 获取当前时间戳
timeTuple = time.localtime(times) # 时间戳转换为时间元组
timeChar = time.strftime('%Y.%m.%d. %H:%M:%S', timeTuple)
print(timeChar)

"""
练习2：
    时间字符串 > 时间元祖 > 时间戳 
"""
time_char = '2019.04.12. 09:05:05'
time_tuple = time.strptime(time_char, '%Y.%m.%d. %H:%M:%S')
print(time.mktime(time_tuple))