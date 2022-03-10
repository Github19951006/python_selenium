"""
@Project ：study 
@Author : 文跃锐（yuerwen）
@Time   : 2022/01/29
@File   :test.py
"""

'''
# 这个函数没有返回值
def func(path1,path2):
	ret = path1 + path2
	print(ret)

ret_ = func(2,6)
print(ret_)  # 返回的结果None
'''

'''
# 统计超过指分数的学生人数
student_list = [50,60,88,98,47,86,78,79,69,59,67,76,73,61,63,38,48]

def scort(st_list,score):
	count = 0
	for sc in student_list:
		if score > sc:
			count += 1
	return count

ret = scort(student_list,90)
print(f'超过指分数的学生人数:{ret}')
'''

'''
# test 4
def get_name_age(nameStr,ageStr):
	name = nameStr[-2:]
	age  = ageStr[-2:]
	result = name + ':' + age
	return result

print(get_name_age(nameStr= '他的名字是：关羽',ageStr= '他的年龄是：28'))
print(get_name_age('他的名字是：刘邦','他的年龄是：28'))
'''


	