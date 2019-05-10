def test_1():

    print("*" * 50)


def test_2():

    print("-" * 50)

    # 函数的嵌套调用
    test_1()

    print("-" * 50)


test_2()