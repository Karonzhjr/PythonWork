import cards_tools

# 无限循环，由用户主动决定什么时候退出循环！
while True:

    # 显示功能菜单
    cards_tools.show_menu()

    # 没有使用 int 转换用户的输入，可以避免一旦用户输入的不是数字，导致程序运行出错
    action_str = input("请选择您希望执行的操作：")
    print("您选择的操作是【%s】" % action_str)

    # 1,2,3 针对名片的操作 if action_str == "1" or action_str == "2" or action_str == "3":
    if action_str in ["1", "2", "3"]:  # 使用 in 针对 列表 判断，避免使用 or 拼接复杂的逻辑条件

        # 新增名片
        if action_str == "1":
            cards_tools.new_card()  # 使用 pass 的作用：（1）占位语句；（2）保持程序结构的完整。
        # 显示全部
        elif action_str == "2":
            cards_tools.show_all()
        # 查询名片
        elif action_str == "3":
            cards_tools.search_card()

    # 0 退出系统
    elif action_str == "0":

        print("欢迎再次使用【名片管理系统】")

        break
        # 如果在开发程序时，不希望立刻执行编写分支内部的代码
        # 可以使用 pass 关键字，表示一个占位符，能够保证程序的代码结构正确！
        # 程序运行时，pass关键字不会执行任何的操作！
        # pass

    # 其他内容输入错误，需要提示用户
    else:
        print("您输入的不正确， 请重新选择")

