"""
3、上机题
    定义一个函数，将列表作为参数传递给函数，并对列表元素进行修改。
"""


def modify_list(unmodified_list):
    """修改列表中的元素

    :param unmodified_list: 待修改的列表
    """
    name_list[0] = "ZhangSan"

    print(unmodified_list)


name_list = ["张三", "李四", "王五", "陈六"]

modify_list(name_list)