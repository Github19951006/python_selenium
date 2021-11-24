"""
@Project ：python 
@Author : 文跃锐（yuerwen）
@Time   : 2021/10/28
@File   :yuerwen_01_test.py
"""
yuer_str = '''Python3 高级开发工程师 上海互教教育科技有限公司上海-浦东新区2万/月02-18满员
测试开发工程师（C++/python） 上海墨鹍数码科技有限公司上海-浦东新区2.5万/每月02-18未满员
Python3 开发工程师 上海德拓信息技术股份有限公司上海-徐汇区1.3万/每月02-18剩余11人
测试开发工程师（Python） 赫里普（上海）信息科技有限公司上海-浦东新区1.1万/每月02-18剩余5人
Python高级开发工程师 上海行动教育科技股份有限公司上海-闵行区2.8万/月02-18剩余255人
python开发工程师 上海优似腾软件开发有限公司上海-浦东新区2.5万/每月02-18满员
'''
'''
# 返回是list对象
split_list = yuer_str.splitlines()

for one in split_list:
	# 返回下标值
	ind = one.find('万/月')
	if ind < 0:
		ind = one.find('万/每月')
		if ind < 0 :
			continue
	print(ind)
'''

# 使用正则表达式
import re
p = re.compile(r'([\d.]+)万/每{0,1}月')
print(p.findall(yuer_str))
