# -*- coding: utf-8 -*-
# 定义默认参数要牢记一点：默认参数必须指向不变对象！
def move(n,a,b,c):
	print('====',n,a,b,c,'=====')
	if n==1:
		print(a,'-->',c)
	else:
		move(n-1,a,c,b)
		print('====',n,a,b,c,'=====')
		move(1,a,b,c)
		print('====',n,a,b,c,'=====')
		move(n-1,b,a,c)
		print('====',n,a,b,c,'=====')
move(3,'A','B','C')