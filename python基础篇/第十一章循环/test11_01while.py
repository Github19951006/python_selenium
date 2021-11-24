"""
@Author : 文跃锐（yuerwen）
@Time   : 2021/08/07
@File   :test11_01while.py
"""
'''
# while 循环
number = input('请输入值：')
while number != 'exit':
    print(f"你输入的是{number}")
    number = input('请重新输入值：')
'''

'''
i = 1
while i <= 1000:
    print(i)
    i += 1
'''

# 使用 while循环对列表进行循环遍历
newList = ['小王:17', '小赵:16', '小李:17', '小孙:16', '小徐:18']
# 1、设置索引游标
dix = 0
# 通过比较比较长度
while dix < len(newList):
    print(newList[dix])
    dix += 1
range()
