"""
@Author : 文跃锐（yuerwen）
@Time   : 2021/08/08
@File   :test11_10练习附加字符串格式化.py
"""
'''
题目2 字符串格式化
现有 公司员工的薪资记录，存储在这样的字符串中

salaryTxt = '
name: Jack   ;    salary:  12000
 name :Mike ; salary:  12300
name: Luk ;   salary:  10030
  name :Tim ;  salary:   9000
name: John ;    salary:  12000
name: Lisa ;    salary:   11000
'
每个员工一行，记录了员工的姓名和薪资， 每行记录 原始文件中并不对齐，中间有或多或少的空格
现要求实现一个python程序，计算出salaryTxt中所有员工的税后工资（薪资的90%）和扣税明细，如下所示

name: Jack   ;    salary:  12000 ;  tax: 1200 ; income:  10800
name: Mike   ;    salary:  12300 ;  tax: 1230 ; income:  11070
name: Luk    ;    salary:  10030 ;  tax: 1003 ; income:   9027
name: Tim    ;    salary:   9000 ;  tax:  900 ; income:   8100
name: John   ;    salary:  12000 ;  tax: 1200 ; income:  10800
name: Lisa   ;    salary:  11000 ;  tax: 1100 ; income:   9900
要求像上面一样的对齐 tax 表示扣税金额和 income表示实际收入。注意扣税金额和 实际收入要取整数
'''

salaryTxt = '''
name: Jack   ;    salary:  12000
 name :Mike ; salary:  12300
name: Luk ;   salary:  10030
  name :Tim ;  salary:   9000
name: John ;    salary:  12000
name: Lisa ;    salary:   11000
'''
# 将字符串按行取出，存到列表中
newList = salaryTxt.splitlines()
# 创建空列，目的：将不为空的元素存储到这个列表中
listAge = []
# 循环遍历取出
for num in newList:
    # 去除空格
    num = num.replace(' ','')
    # 判断空行
    if num != '':
        # 将元素追加到列表的最后
        listAge.append(num)

# 遍历循环过滤后的列表
for name in listAge:
    # 将字符串进行切割，多个变量同时赋值
    name,salary = name.split(";")

    name = name.split(':')[-1]
    salary = salary.split(':')[-1]

    # 计算税收 salaryInt 表示税前工资
    salaryInt = int(salary)
    # 计算出税后薪资 income 表示税后工资
    income = salaryInt * 75 / 100
    # tax 表示税费
    tax = salaryInt - income
    # 打印结果
    print(f'name: {name:<8};  salary:{salaryInt:8};  tax:{tax:8.0f};  income:{income:8.0f}')

