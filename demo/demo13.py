#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'a test demo13'
__author__='XYD'
import math

def fn(num):
    i = int(math.sqrt(num))
    for n in range(2,i+1):
        if num % n ==0:
            return False
    return True

m,n = [int(x) for x in input().split(' ')]
num = 0
init = 3
primes = []
while True:
    if m == 1:
        primes.append(2)
        num += 1
    elif fn(init):
        num += 1
        if num >= m-1 and num < n:
            primes.append(init)
        if num == n:
            break
    init += 2
primes = [str(i) for i in primes]
print("\n".join([i + 10 > len(primes) and " ".join(primes[i:]) or " ".join(primes[i:i+10]) for i in range(len(primes)) if i % 10 == 0]))
    
