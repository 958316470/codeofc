#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'a test demo10'
__author__='XYD'


count = int(input())
l = []
j = 0
for i in range(count):
	j = j + 1
	numstr = input()
	a,b,c=numstr.split(' ')
	if int(a) + int(b) > int(c):
		print('Case #%d: true' % j)
	else:
		print('Case #%d: false' % j)

	