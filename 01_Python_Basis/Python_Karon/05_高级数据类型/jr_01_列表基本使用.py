name_list = ["zhangsan", "lisi", "wangwu"]

# 1. 取值和取索引值
print(name_list[2])
print(name_list.index("lisi"))

# 2. 修改
name_list[1] = "李四"

# 3. 增加
# (1) append方法可以在列表末尾追加数据
name_list.append("王小二")
# (2) insert方法可以在列表的指定索引位置插入数据
name_list.insert(1, "小美眉")
# (3) extend方法可以把其他列表中的完整内容追加到当前列表的末尾
temp_list = ["孙悟空", "猪二哥", "沙师弟"]
name_list.extend(temp_list)

# 4. 删除
name_list.remove("wangwu")
name_list.pop()
name_list.pop(5)
name_list.clear()

print(name_list)