"""
@Author : 文跃锐（yuerwen）
@Time   : 2021/08/06
@File   :test10_02fString.py
"""
salary = input("请输入薪资：")   # 注意的点：字符串是不支持右对齐的
num = int(salary)
# 计算税额
tax = int(salary) * 25/100
srSalary = int(salary) * 75/100
# 右对齐的打印
print(f'税前薪资是：{num:8}元， 缴税：{tax:8}元， 税后薪资是：{srSalary:8}元')
# 左对齐
print(f'税前薪资是：{num:<8}元， 缴税：{tax:<8}元， 税后薪资是：{srSalary:<8}元')

# 右对齐补零
print(f'税前薪资是：{num:<08}元， 缴税：{tax:08}元， 税后薪资是：{srSalary:08}元')
# 员工 1                                                     .
salary = 800
tax = int(salary) *25/100
aftertax = int(salary) *75/100
print(f'税前薪资是：{salary:8}元， 缴税：{tax:8}元， 税后薪资是：{aftertax:8}元')


# 员工 2
salary = 150
tax = int(salary) *25/100
aftertax = int(salary) *75/100
print(f'税前薪资是：{salary:8}元， 缴税：{tax:8}元， 税后薪资是：{aftertax:8}元')


# 员工 3
salary = 100000
tax = int(salary) *25/100
aftertax = int(salary) *75/100
print(f'税前薪资是：{salary:8}元， 缴税：{tax:8}元， 税后薪资是：{aftertax:8}元')