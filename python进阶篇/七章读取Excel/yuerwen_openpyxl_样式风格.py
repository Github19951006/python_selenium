"""
@Project ：python 
@Author : 文跃锐（yuerwen）
@Time   : 2021/11/12
@File   :yuerwen_openpyxl_样式风格.py
"""
import openpyxl
from openpyxl.styles import colors, Font

# 加载Excel 对象
book = openpyxl.load_workbook('income-1.xlsx')

# 获取sheet 对象
sheet = book['2018']

# 指定单元格的样式风格
# sheet['A1'].font = Font(colors = colors.RED,size = 15,bold = True,italic = True)
# 指定单元格字体颜色，
sheet['A1'].font = Font(color=colors.BLACK, #使用预置的颜色常量
                        size=15,    # 设定文字大小
                        bold=True,  # 设定为粗体
                        italic=True # 设定为斜体
                        )

sheet['B1'].font = Font(color = '981818')

# 指定整列 字体风格， 这里指定的是第2列
font = Font(bold=True)
for x in range(1, 100): # 第 1 到 100 行
    sheet.cell(row=x, column=2).font = font
book.save('income-1.xlsx')