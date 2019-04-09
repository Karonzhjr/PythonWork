"""
题目3:
    访客：编写一个程序，提示用户输入其名字；用户作出响应后，将其名字写入到文件guest.txt 中。
"""
while True:
    name = input('请输入您的姓名：')
    if name == 'no':
        print('输入完毕')
        break
    else:
        with open('guest.txt', 'a+', encoding = 'utf-8') as files:
            """
            # 疑问：guest.txt 与 files 是什么关系？名字写入到files中，为什么会传入guest.txt中呢？
            """
            files.write(name)  # 把名字写入文件
            files.write('\n')  # 写完后换行
            files.seek(0)      # 重置指针到文件开头位置
            content = files.read()  # 读文件内容
            print(content)   # 打印内容

