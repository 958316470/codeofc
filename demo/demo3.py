# -*- coding: utf-8 -*-
# 定义默认参数要牢记一点：默认参数必须指向不变对象！
def power(x, n=2):
	s = 1;
	while n > 0:
		n = n -1
		s = s * x
	return s
print(power(5))
print(power(5,3))