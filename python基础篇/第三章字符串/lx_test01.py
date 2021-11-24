"""
@Author : 文跃锐（yuerwen）
@Time   : 2021/07/28
@File   :lx_test01.py
"""

'''
你们公司每月的净利润计算公式如下
( 总收入 -  会计小王薪资  - 餐饮费 - 交通费 ) * 80%税费剩余
请大家写Python程序，合理的使用变量 和注释 ，计算 并 打印出 每月的净利润。
具体的 收入和支出 数值，使用input函数，让用户输入。
'''
# 总收入
inSum = int(input("总收入："))
# 会计小王薪资
inSalary = int(input("小王薪资:"))
# 餐饮费
inDinner_fee = int(input("餐饮费:"))
# 交通费
inTransportation_fee = int(input("交通费:"))

total = str((inSum - inSalary - inDinner_fee - inTransportation_fee) * 0.8)
print("本月的净利润为：" + total)
