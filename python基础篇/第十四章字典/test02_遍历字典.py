"""
@Author : 文跃锐（yuerwen）
@Time   : 2021/08/18
@File   :test02_遍历字典.py
"""
'''
知识点：访问字典的所有元素
'''
# 创建一个字典
dic = {
	'account1'  : 13 ,
    'account2'  : 12 ,
    'account3'  : 15 ,
}
# items方法，返回的是一个类似列表一样的对象，其中每个元素就是 键值组成的元组
print(dic.items())  # dict_items([('account1', 13), ('account2', 12), ('account3', 15)])

for key,val in dic.items():
	print(f'{key} =::= {val}')
	