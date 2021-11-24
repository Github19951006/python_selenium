"""
@Author : 文跃锐（yuerwen）
@Time   : 2021/09/16
@File   :yuerwen_test3.py
"""
import time
# for循环n次   使用内置函数rang()
for n in range(10):
	print(n+1)

start = time.time()
for n in range(50,101,1):
	print(n)
	end = time.time()
print(end - start)

studentAges = ['小王:17', '小赵:16', '小李:17', '小孙:16', '小徐:18']

# enumerate (studentAges) 每次迭代返回 一个元组
# 里面有两个元素，依次是 元素的索引和元素本身
for idx, student in enumerate(studentAges):
    if int(student.split(':')[-1]) > 17:
        print(idx)
        print(type(student.split(':')[-1]))