"""
@Project ：python 
@Author : 文跃锐（yuerwen）
@Time   : 2021/11/07
@File   :yuerwen_02_表单对象.py
"""
import xlrd
# 打开Excel表 返回book对象
book = xlrd.open_workbook('income.xlsx')

# 表单索引从0开始，获取第一个 表单对象 <xlrd.sheet.Sheet object at 0x000001D58C387B80>
sheet_index = book.sheet_by_index(0)
print(sheet_index)

# 获取表单名字为2018的表单对象 <xlrd.sheet.Sheet object at 0x0000018EE2407B50>
sheet_name = book.sheet_by_name('2018')
print(sheet_name)

# 获取所有的表单对象，放入一个列表返回
# [<xlrd.sheet.Sheet object at 0x0000023FB4717100>, <xlrd.sheet.Sheet object at 0x0000023FB4717B50>, <xlrd.sheet.Sheet object at 0x0000023FB4717B20>]
sheet_all = book.sheets()
print(sheet_all)
