"""
@Author : 文跃锐（yuerwen）
@Time   : 2021/08/08
@File   :test11_04列表推导式.py
"""
# 要求：将第一个列表的值变成平方，存储到第二个列表中
newList1 = [1,2,3,4,5,6,7]
# 列表推导式
copyList2 = [num ** 2 for num in newList1]
print(copyList2)