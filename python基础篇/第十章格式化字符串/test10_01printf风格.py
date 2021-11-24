"""
@Author : 文跃锐（yuerwen）
@Time   : 2021/08/04
@File   :test10_01printf风格.py

%s是一种格式化符号， Python 解释器 看到 %s ， 就会调用内置函数 str()，
并将对应的 格式化对象 作为 参数传入 ， 返回的结果字符串填入对应占位符。
"""
# printf风格
# salary = input("请输入薪资：")

# 计算税额
# tax = int(salary) * 25/100
# srSalary = int(salary) * 75/100
# print('税前薪资：%s元，缴税：%s元，税后薪资：%s元' %(salary,tax,afterSalary))

# 左对齐的打印
print('税前薪资：%-10s 元' % 100000.9)
print('税前薪资：%-10s 元' % 1000)
print('税前薪资：%-10s 元' % 100)

# 右对齐的打印
print('税前薪资：%10s 元' % 100000)
print('税前薪资：%10s 元' % 1000)
print('税前薪资：%10s 元' % 100)

print('税前薪资：%010d 元' % (100000))
print('税前薪资：%010d 元' % 1000)
print('税前薪资：%010d 元' % 100)