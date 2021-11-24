"""
@Author : 文跃锐（yuerwen）
@Time   : 2021/07/28
@File   :test06.py
"""

salary = input("请输入薪资：")
# 先将键入的数据转换成int类型
inSalary = int(salary)

# 计算出税后的薪资
reaSalary = inSalary * 75/100

# 再转换成字符串，方便下面的字符串的拼接
reaSalaryStr = str(reaSalary)

print('税后薪资是：' + reaSalaryStr)
# print(type(salary))  # <class 'str'>  键盘输入的数据类型是字符串

