"""
@Author : 文跃锐（yuerwen）
@Time   : 2021/09/17
@File   :yuerwen_test_冒泡算法.py
"""
arr = [23, 41, 25, 54, 18, 14]
length = len(arr)

for i in range(0,length-1): # 0\1\2\3\4
	if arr[i] > arr[i+1]:
		arr[i],arr[i+1] = arr[i+1],arr[i]

		









