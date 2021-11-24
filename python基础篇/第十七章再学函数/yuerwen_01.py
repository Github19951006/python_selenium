"""
@Author : 文跃锐（yuerwen）
@Time   : 2021/09/13
@File   :yuerwen_01_序列化.py
"""
var = '桌子'

def test():
	var = '椅子'
	print(f'函数内的，var的值：{var}')
	
# 调用函数
test()

print(f'函数外的，var的值：{var}')