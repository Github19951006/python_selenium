"""
@Project ：python 
@Author : 文跃锐（yuerwen）
@Time   : 2021/11/10
@File   :yuerwen_test_openpyxl_列表元组2.py
"""
# 如果你的数据在一个列表或者元组中，可以使用append方法在sheet的末尾添加新行，写入数据

import openpyxl

name2Age = [
    ('张飞' ,  38 ) ,
    ('赵云' ,  27 ) ,
    ['许褚' ,  36 ] ,
    ['典韦' ,  38 ] ,
    ['关羽' ,  39 ] ,
    ['黄忠' ,  49 ] ,
    ['徐晃' ,  43 ] ,
    ['马超' ,  23 ]
]
rows = (
   (88, 46, 57),
   (89, 38, 12),
   (23, 59, 78),
   (56, 21, 98),
   (24, 18, 43),
   (34, 15, 67)
)

# 创建一个Excel workbook 对象
book = openpyxl.Workbook()
sh = book.active
sh.title = '年龄表'

# 写标题栏
sh['A1'] =  '姓名'
sh['B1'] =  '年龄'

for row in name2Age:
    # 添加到下一行的数据
    sh.append(row)
    # print(sh.append(row))
for row in rows:
    # 添加到下一行的数据
    sh.append(row)
    # print(sh.append(row))

# 保存文件
book.save('信息.xlsx')