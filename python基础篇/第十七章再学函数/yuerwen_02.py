"""
@Author : 文跃锐（yuerwen）
@Time   : 2021/09/14
@File   :yuerwen_02.py
"""
'''
前面加一个星号的参数，称之为可变参数
'''
studentInfo = {
    '张飞' :  18,
    '赵云' :  17,
    '许褚' :  16,
    '典韦' :  18,
    '关羽' :  19,
}
'''
def printAge(student):
	for stu in student:
		print( f'学生：{stu} , 年龄 {studentInfo[stu]}')

# printAge(['张飞', '典韦', '关羽'])

# 改为
# 会报错：TypeError: printAge() takes 1 positional argument but 3 were given
printAge('张飞', '典韦', '关羽')
printAge(['赵云'])
'''

# 优化，前面加一个星号的参数，称之为可变参数
# 理解：在调用该函数的时候，Python解释器会创建一个 tuple 赋值给这个参数变量。并且会把 传入的数据对象 放到这个tuple对象里面
def printAge(*student):
	for stu in student:
		print(f'学生：{stu} , 年龄 {studentInfo[stu]}')
		
printAge('张飞', '典韦', '关羽')
printAge('赵云')