"""
@Project ：python 
@Author : 文跃锐（yuerwen）
@Time   : 2021/10/28
@File   :yuerwen_02_反序列化.py
"""

import json

historyTransactions = [
    {
        'time'   : '20170101070311',  # 交易时间
        'amount' : '3088',            # 交易金额
        'productid' : '45454455555',  # 货号
        'productname' : 'iphone7'     # 货名
    },
    {
        'time'   : '20170101050311',  # 交易时间
        'amount' : '18',              # 交易金额
        'productid' : '453455772955', # 货号
        'productname' : '奥妙洗衣液'   # 货名
    },
]

# 序列化
obj_json = json.dumps(historyTransactions,ensure_ascii=False,indent=4)
print(type(obj_json))  # <class 'str'>
print(obj_json)

# 反序列化
object_List = json.loads(obj_json)
print(type(object_List))  # <class 'list'>
print(object_List)