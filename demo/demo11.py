#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'a test demo11'
__author__='XYD'
def fn(n):
	if n==0:
		return 'N'
	return n


L = [0,0,0,0,0]
m=0
ind = 0
numStr = input().split(' ')
count = int(numStr[0]) + 1
for i in range(1,count):
	num = int(numStr[i])
	flag = num % 5
	if flag == 4 and num > L[4]:
		L[4] = num
	elif flag == 3:
		m += 1
		L[3] += num
	elif flag == 2:
		L[2] += 1
	elif flag == 1:
		if ind % 2 == 0:
			L[1] += num
		else:
			L[1] -= num
		ind += 1
	elif flag == 0 and num % 2 == 0:
		L[0] += num
	
if L[3] != 0:
	L[3] = round(L[3] / m,1)
L = list(map(fn,L))
print('%s %s %s %s %s' % (L[0],L[1],L[2],L[3],L[4]))


   
	
	

	