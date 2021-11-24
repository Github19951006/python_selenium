"""
@Author : 文跃锐（yuerwen）
@Time   : 2021/09/14
@File   :yuerwen_03.py
"""
def addStudent(table,**students):
	print(type(students))
	for name,age in students.items():
		table[name] = age
		
table1 = {}
table2 = {}
addStudent(table1,yuer = 17,hais = 27)
addStudent(table2, 李白=20, 杜甫=24,yunjing = 77)
print(table1)
print(table2)