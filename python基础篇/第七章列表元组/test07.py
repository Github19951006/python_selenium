"""
@Author : 文跃锐（yuerwen）
@Time   : 2021/07/29
@File   :test07.py
"""

# 创建列表
newlist = [1,2,3.14,'hello',[2,3,4]]
# 获取列表的指定值,通过索引
newlist[1]
print(newlist[1])

a=newlist[-1][1]
print(a)

# 切片
b = newlist[0:3]
print(b)
c=newlist[-1][:2]
print(c)