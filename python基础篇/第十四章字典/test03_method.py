"""
@Author : 文跃锐（yuerwen）
@Time   : 2021/08/20
@File   :test03_method.py
"""
'''
字典常用的方法：
1、clear()  清楚字典全部内容
2、get()  根据key来获取values
3、update() 使用一个字典包含key-values进行更新已有的数据。如果没有就更新，没有就添加；
4、items() 返回的是一个类似列表一样的对象，其中每个元素就是 键值组成的元组
5、keys() 将字典 所有的 键 存入的 一个类似列表的对象
6、values()  将字典 所有的 值 存入的 一个类似列表的对象
7、len() 计算字典的格式
'''
# 创建字典
dic = {}

# var[key] = something 添加字典
dic['数学'] = 99
dic['语文'] = 122
dic['道法'] = 90
print(dic) # {'数学': 99, '语文': 122, '道法': 90}

# clear  清除字典内容
# dic.clear()


# get 通过key来获取values的值
ret = dic.get('数学')
print(f'values的值 : {ret}') # 99

# update 使用一个字典包含key-values进行更新已有的数据。如果没有就更新，没有就添加；
newDic = {'历史':99,'化学':88,'语文':109}
dic.update(newDic)
print(dic)  # {'数学': 99, '语文': 109, '道法': 90, '历史': 99, '化学': 88}

# items() items方法，返回的是一个类似列表一样的对象，其中每个元素就是 键值组成的元组
for account,level in dic.items():
    print (f'{account} =:= {level}')
    
# keys()  将字典 所有的 键 存入的 一个类似列表的对象
dKey = dic.keys()
print(dKey)  # dict_keys(['数学', '语文', '道法', '历史', '化学'])

# values  将字典 所有的 值 存入的 一个类似列表的对象
dValues = dic.values()
print(dValues) # dict_values([99, 109, 90, 99, 88])

print(f'字典的长度：{len(dic)}')