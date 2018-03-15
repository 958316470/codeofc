#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'a test demo12'
__author__='XYD'

def fib():
    m = 1
    while True:
        m += 2
        yield m

def filternum(n):
    return lambda x: x % n > 0

def primes():
    yield 2
    it = fib()
    while True:
        n = next(it)
        yield n
        it = filter(filternum(n),it)
num = primes()
m,n = input().split(' ')
count=0
res=''
for i in range(int(n)):
	x = next(num)
	if i >= int(m)-1:
		res+=str(x)
		count += 1
		if count % 10 == 0:
			res+='\n'
		else:
			res+=' '
res = res.strip()
print(res)
