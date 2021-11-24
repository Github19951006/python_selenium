"""
@Author : 文跃锐（yuerwen）
@Time   : 2021/08/12
@File   :test12_附加练习2.py
"""
'''
网址=后面 https://www.bilibili.com/video/av74106411/?p=99后33面还有?内容
地址 https://www.bilibili.com/video/av74106411/?p=9还有?内
https://www.bilibili.com/video/av74106411/?p=199还有?内容
写一个程序，做到如下功能：
让用户输入一个数字，比如用户输入3， 程序就可以修改该文件，把文件中所有的链接末尾数字都加上3
'''
'''
伪代码：
1、open() 打开文件并读取
2、将字符串 按行获取到列表中  readlines()
3、定位数字的位置
    3.1 用find()方法定位到 https://www.bilibili.com/video/av74106411/?p= 的索引位置location
    3.2 得到数字的起始位置 locationStar = location + len(https://www.bilibili.com/video/av74106411/?p=)
    3.3 得到数字结束的位置 locationEnd 
        3.3.1 while循环判断 locationStar开始后的每个字符isdigit() 
    3.4 得到具体的数字 number[locationStar:locationEnd]
4、将字符串拼接 number[:locationStar] + 替换的数字 + number[locationEnd:]
5、将拼接的字符串，存储到空字符串中
6、通过w写入文件中

'''
def getNumber(number):
    # 1、open() 打开文件并读取
    with open('prac_filerw.txt','r',encoding='utf8') as f:
        # 2.将字符串按换行符 切割，返回一个列表
        lineTXT = f.readlines()

    # 创建一个空字符串
    newStr = ''

        # 3、定位数字的位置
    for lines in lineTXT:
        # 3.1 用find()方法定位到 https://www.bilibili.com/video/av74106411/?p= 的索引位置location
        location = lines.find('https://www.bilibili.com/video/av74106411/?p=')
        # 判断没有找到的情况
        if location < 0:
            newStr += lines
            continue

        # 3.2 得到数字的起始位置 locationStar = location + len(https://www.bilibili.com/video/av74106411/?p=)
        locationStar = location + len('https://www.bilibili.com/video/av74106411/?p=')

        #3.3 得到数字结束的位置 locationEnd
            # 3.3.1 循环判断 locationStar开始后的每个字符isdigit()
        locationEnd = locationStar
        while lines[locationEnd].isdigit():
            locationEnd += 1

        # 3.4 得到具体的数字 number[locationStar:locationEnd]
        numberRet = int(lines[locationStar:locationEnd]) + number
        # 4、将字符串拼接 lines[:locationStar] + 替换的数字 + lines[locationEnd:]
        str2 = lines[:locationStar] + str(numberRet) + lines[locationEnd:]

        # 5、将拼接的字符串，存储到空字符串中
        newStr += str2
    # 6、通过w写入文件中
    with open('prac_filerw1.txt','w',encoding='utf') as f:
        f.write(newStr)

# 调用函数
number = int(input('输入一个数字:'))
getNumber(number)