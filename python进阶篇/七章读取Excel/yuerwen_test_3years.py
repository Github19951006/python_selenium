"""
@Project ：python 
@Author : 文跃锐（yuerwen）
@Time   : 2021/11/08
@File   :yuerwen_test_3years.py
"""

import xlrd
book = xlrd.open_workbook('income.xlsx')

sheets = book.sheets()

income_of_3years = 0

for sheet in sheets:
	# 获取列的所有数据，返回list
	colx_incomes = sheet.col_values(colx=1, start_rowx=1)
	print(f'{sheet.name}年所有工资的总和：{sum(colx_incomes)} 元')
	
	# 算法：去除带*的月份的工资
	# 初始指定工资
	start_incomes = 0
	# 月份在第1列
	monthes = sheet.col_values(colx=0)
	
	for row, month in enumerate(monthes):
		if type(month) is str and month.endswith('*'):
			incomes = sheet.cell_value(row, 1)
			print(month, incomes)
			start_incomes += incomes
	
	print(f"{sheet.name}年去除带*后真实收入为: {int(sum(colx_incomes) - start_incomes)} 元")
	income_of_3years += int(sum(colx_incomes) - start_incomes)
	
print('-----------------------------------------------------------------------')
print(f'全部收入为{income_of_3years}')