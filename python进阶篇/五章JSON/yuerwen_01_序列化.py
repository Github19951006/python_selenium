"""
@Project ：python 
@Author : 文跃锐（yuerwen）
@Time   : 2021/10/27
@File   :yuerwen_01_序列化.py
"""
# 导入json
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
# dumps(格式化的变量名)
# ensure_ascii=False 如果没有这个参数，得到的json中文字就会以Unicode的显示
# indent=4 缩进打印
# 序列化  ：程序的各种类型数据对象 变成 表示该数据对象的 字节串
object_json = json.dumps(historyTransactions,ensure_ascii=False,indent=4)
print(object_json)
print(type(object_json))  # <class 'str'>

'''
格式化成json后的：
[{
	"time": "20170101070311",
	"amount": "3088",
	"productid": "45454455555",
	"productname": "iphone7"
}, {
	"time": "20170101050311",
	"amount": "18",
	"productid": "453455772955",
	"productname": "奥妙洗衣液"
}]
'''

'''
总结：
1、执行前：historyTransactions 是一个列表对象，格式化之后是一个字符串对象 ====类型改变
2、
'''