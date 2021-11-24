"""
@Author : 文跃锐（yuerwen）
@Time   : 2021/08/14
@File   :test01.py
"""
# 导包
import test01_link
'''
我们开发一个程序，记录每人的账单，月末可以结算
把 输入总费用和聚餐人员，计算人均费用 的功能
'''
# 键入用餐的费用
free = input("请输入用餐的费用：")
# 输入用餐人名，逗号隔开
names = input('请输入用餐人名（逗号隔开）：')

# 将输入的字符串以’，‘分割，返回列表
nameList = names.split(',')

# 统计人数
namesNumber = len(nameList)

# 计算人均费用
avgFree = int(free)/namesNumber
print(avgFree)

# 使用 模块save里面的 savetofile 函数
test01_link.savetofile(nameList, avgFree)