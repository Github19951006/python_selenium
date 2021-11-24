"""
@Author : 文跃锐（yuerwen）
@Time   : 2021/08/18
@File   :test01.py
"""
# 定义空字典
dic = {}
print(dic)
print(type(dic)) # <class 'dict'>

'''
添加语法：
var[key] = something
'''
# 赋值语句  添加元素
dic['one'] = 1
print(dic) # {'one': 1}
dic['two'] = 2
print(dic)
# 修改
dic['two'] = 4
print(dic)

'''
删除语句：
del var[key]
'''
# 删除
del dic['one']
print(dic)

if 'two' in dic:
	print('two 在字典中存在')