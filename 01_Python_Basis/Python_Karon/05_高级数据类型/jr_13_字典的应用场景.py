"""
使用多个键值对描述一个物体的相关信息
    ————描述更复杂的数据信息，将多个字典放在一个列表中，在进行遍历
"""
card_list = [
    {"name": "张三",
     "QQ": 666888,
     "Phone": 15866668888},
    {"name": "李四",
     "QQ": 999666,
     "Phone": 13299995555}
]

for card_info in card_list:

    print(card_info)