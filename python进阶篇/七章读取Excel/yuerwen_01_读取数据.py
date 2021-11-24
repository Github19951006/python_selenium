"""
@Project ：python 
@Author : 文跃锐（yuerwen）
@Time   : 2021/11/05
@File   :yuerwen_01_读取数据.py
"""
import xlrd

'''
理解：book 对象是 Excel对象
'''
book = xlrd.open_workbook("income.xlsx")
print(type(book))  # <class 'xlrd.book.Book'> book对象


'''
理解：sheet对象  表单对象
可以根据表单的索引 或者 表单名获取 表单对象，使用如下对应的方法
nsheets:        表单的数量 int
sheet_names():  表单的名称 返回List
'''
print(f"包含表单数量 {book.nsheets}")
print(f"表单的名分别为: {book.sheet_names()}")

# 返回的是表单对象
index = book.sheet_by_index(0)    # <xlrd.sheet.Sheet object at 0x0000029EB3BC7100>
name = book.sheet_by_name('2018') # <xlrd.sheet.Sheet object at 0x000001DFE3407100>
# 获取所有的表单对象，放入一个列表返回
book.sheets() # [<xlrd.sheet.Sheet object at 0x00000186E8437100>, <xlrd.sheet.Sheet object at 0x00000186E8437B50>, <xlrd.sheet.Sheet object at 0x00000186E8437B20>]
