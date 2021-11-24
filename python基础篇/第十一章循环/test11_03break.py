"""
@Author : 文跃锐（yuerwen）
@Time   : 2021/08/08
@File   :test11_03break.py
"""
'''
# 普通的判断
command = input("请输入命令:")
while command != 'exit':
    print(f'输入的命令是{command}')
    command = input("请输入命令")

print('程序结束')
'''
# 改进后的
while True:
    command = input("请输入命令:")
    if command == 'exit':
        # break 是跳出循环体的
        break
    print(f'输入的命令是{command}')

print('程序结束')