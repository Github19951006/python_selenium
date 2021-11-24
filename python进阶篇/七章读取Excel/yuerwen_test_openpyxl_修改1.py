"""
@Project ：python 
@Author : 文跃锐（yuerwen）
@Time   : 2021/11/11
@File   :yuerwen_test_openpyxl_修改1.py
"""
import openpyxl

# 加载Excel表
l_book = openpyxl.load_workbook('income.xlsx')

# 得到sheet对象
sheet = l_book['2017']

# 修改内容
sheet['A1'] = '修改一下'

# 存储Excel文件
l_book.save('income-1.xlsx')