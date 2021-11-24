"""
@Project ：python 
@Author : 文跃锐（yuerwen）
@Time   : 2021/11/07
@File   :yuerwen_03_表单对象方法.py
"""
'''
前提是获取到表单对象之后才有这些方法：
表单行数（nrows）
列数（ncols）
表单名（name）
表单索引（number）
'''

import xlrd

book = xlrd.open_workbook('income.xlsx')
# 通过下标索引，获取表单对象
obj_sheet = book.sheet_by_index(0)

print(f'表单行数量：{obj_sheet.nrows}')
print(f'表单列数量：{obj_sheet.ncols}')
print(f'表单名字：{obj_sheet.name}')
print(f'表单索引：{obj_sheet.number}')

# 理解： cell_value(（行x）rowx=0,（列y）colx=0)  指定获取某个单元格的内容
sheet_text = obj_sheet.cell_value(rowx=3,colx=1)
print(f'第一行第一列的内容：{sheet_text}')

# 获取表单中 某一行的所有内容 row_value(rowx = ) 返回的是list
row_sheet = obj_sheet.row_values(rowx=0)
print(f'指定行的所有数据：{row_sheet}')

# 获取表单中 某一列的所有内容 col_value(colx = ) 返回的是list
colx_sheet = obj_sheet.col_values(colx=0,start_rowx=1)
print(f'指定列的所有数据：{colx_sheet}')