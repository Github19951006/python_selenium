"""
@Author : 文跃锐（yuerwen）
@Time   : 2021/08/08
@File   :test11_02for.py
"""
'''
newList = ['小王:17', '小赵:16', '小李:17', '小孙:16', '小徐:18']
# for循环遍历
for num in newList:
    print(num[0:2])
#    print(type(num))

# range(start,end,步长)
for n in range(6,11,3):
    print(n)
'''
studentAges = ['小王:17', '小赵:16', '小李:17', '小孙:16', '小徐:18']
# enumerate (studentAges) 每次迭代返回 一个元组
# 里面有两个元素，依次是 元素的索引和元素本身
for idx, student in enumerate(studentAges):
    if int(student.split(':')[-1]) > 17:
        print(idx)
