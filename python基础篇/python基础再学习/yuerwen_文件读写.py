"""
@Author : 文跃锐（yuerwen）
@Time   : 2021/09/17
@File   :yuerwen_文件读写.py
"""
# with open('yuerwen.txt','w',encoding='utf8') as f:
# 	f.write('你好，中国！！加油学python')

# # 使用字节串的方式读取出来
# with open('yuerwen.txt','rb') as f:
# 	ret = f.read()
# # b'\xe4\xbd\xa0\xe5\xa5\xbd\xef\xbc\x8c\xe4\xb8\xad\xe5\x9b\xbd\xef\xbc\x81\xef\xbc\x81\xe5\x8a\xa0\xe6\xb2\xb9\xe5\xad\xa6python'
# print(ret)

# 用字节串的方式写入到文件中
with open('yuerwen.txt','wb') as f:
	f.write('新加入的文字'.encode('utf8'))