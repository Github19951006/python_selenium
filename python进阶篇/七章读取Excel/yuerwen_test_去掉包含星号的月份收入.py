"""
@Project ：python 
@Author : 文跃锐（yuerwen）
@Time   : 2021/11/08
@File   :yuerwen_test_去掉包含星号的月份收入.py
"""
'''
那么我们怎么在汇总收入中，去掉包含星号的月份收入呢？
就需要我们查出哪些月份是带星号的，不要统计在内。
'''
import xlrd

# 打开Excel表格 返回book对象
book = xlrd.open_workbook('income.xlsx')

# 获取表单对象
sheet_obj = book.sheet_by_name('2018')
# 获取列的所有数据，返回list
colx_incomes = sheet_obj.col_values(colx=1, start_rowx=1)
print(f'所有工资的总和：{sum(colx_incomes)} 元')

# 算法：去除带*的月份的工资
# 初始指定工资
start_incomes = 0
# 月份在第1列
monthes = sheet_obj.col_values(colx=0)
	
for row, month in enumerate(monthes):
	if type(month) is str and month.endswith('*'):
		incomes = sheet_obj.cell_value(row, 1)
		print(month, incomes)
		start_incomes += incomes

print(f"2018年真实收入为: {int(sum(colx_incomes)- start_incomes)} 元")

