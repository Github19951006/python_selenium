"""
@Author : 文跃锐（yuerwen）
@Time   : 2021/08/08
@File   :test11_09练习附加质数.py
"""
'''
题目1 列出质数
质数 (素数）是大于1的整数，而且 只可以 被 1 和 自己整除。
请写代码找出 1000 以内的质数
结果参考 https://www.shuxuele.com/prime_numbers.html
'''
# 创建空列表，目的：存储质数
num=[]
# 定义质数函数
def listNumber(leng):
    i=2
    for i in range(2,leng+1):
       j=2
       for j in range(2,i):
          if(i%j==0):
             break
       else:
            num.append(i)
# 调用函数
listNumber(1000)
print(num)

'''
总结：
1、
'''