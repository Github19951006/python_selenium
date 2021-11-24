"""
@Project ：python 
@Author : 文跃锐（yuerwen）
@Time   : 2021/11/12
@File   :yuerwen_openpyxl_增.py
"""

import openpyxl

# 加载Excel 对象
book = openpyxl.load_workbook('income-1.xlsx')

# 通过sheet表的名字 获取sheet对象
sheet = book['2018']

# 增加行 或者 列
# 插入行 insert_rows(行位置，插入的行数)
# 插入列 insert_cols(列位置，插入的列数)
# 在第二行的位置加入1行
sheet.insert_rows(2)

# 删除
# sheet.delete_rows(2)

# 在第二行的位置加入3行
sheet.insert_rows(2,3)

# 删除
# sheet.delete_rows(2,3)

# 在第二列中插入1列
sheet.insert_cols(2)

# 删除
# sheet.delete_cols(2)

# 在第二列的位置加入4列
sheet.insert_cols(2,4)

# 删除
# sheet.delete_cols(2,4)

# 保存Excel文件
book.save('income-1.xlsx')
