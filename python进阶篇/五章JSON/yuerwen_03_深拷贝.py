"""
@Project ：python 
@Author : 文跃锐（yuerwen）
@Time   : 2021/10/28
@File   :yuerwen_03_深拷贝.py
"""

list1 = [
	{
		'name':'yuerwen',
		'age':18,
		'height':188
	},
	{
		'name':'haisliu',
		'age':18,
		'height':166
	}
]

# list2 = list1

# 深拷贝
'''
l = []
for one in list1:
	l.append({'name':one['name'],'height':one['height']})
# print(l[0]['name'] )

list1[0]['name'] = 'ddd'
print(l[0]['name'])
'''

# 使用json的 深拷贝
import json
new_list1 = json.loads(json.dumps(list1,ensure_ascii=False))
list1[0]['name'] = 'ddd'
print(new_list1[0]['name']) # yuerwen