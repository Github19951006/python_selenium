"""
@Project ：python 
@Author : 文跃锐（yuerwen）
@Time   : 2021/11/13
@File   :yuerwen_com_时间差计算.py
"""
import time

def byCom():
    t1 = time.time()
    import win32com.client
    excel = win32com.client.Dispatch("Excel.Application")

    # excel.Visible = True     # 可以让excel 可见
    workbook = excel.Workbooks.Open(r"D:/study/python/python进阶篇/七章读取Excel/income-2.xlsx")

    sheet = workbook.Sheets(2)

    # print(sheet.Cells(2,15).Value)
    print(sheet.UsedRange.Rows.Count)  #多少行

    t2 = time.time()
    print(f'打开: 耗时{t2 - t1}秒')

    total = 0
    for row in range(2,sheet.UsedRange.Rows.Count+1):
        value = sheet.Cells(row,15).Value
        if type(value) not in [int,float]:
            continue
        total += value

    print(total)

    t3 = time.time()
    print(f'读取数据: 耗时{t3 - t2}秒')


def byXlrd():
    t1 = time.time()
    import xlrd

    # 加载 excel 文件
    srcBook = xlrd.open_workbook("income-2.xlsx")
    sheet = srcBook.sheet_by_index(2)

    # print(sheet.cell_value(rowx=1,colx=14))
    print(sheet.nrows) #多少行

    t2 = time.time()
    print(f'打开: 耗时{t2 - t1}秒')

    total = 0
    for row in range(1,sheet.nrows):
        value = sheet.cell_value(row, 2)
        if type(value) == str:
            continue
        total += value

    print(total)

    t3 = time.time()
    print(f'读取数据: 耗时{t3 - t2}秒')

byCom()
byXlrd()