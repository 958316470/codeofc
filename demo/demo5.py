#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 定义默认参数要牢记一点：默认参数必须指向不变对象！
def log(func):
	def wrapper(*args,**kw):
		print('call %s():' % func.__name__)
		return func(*args,**kw)
	return wrapper
@log
def now():
	print('2018-03-08')
now()