# -*- coding: utf-8 -*-
import math
def quadratic(a,b,c):
	m = math.pow(b,2) - 4 * a * c;
	n = - (b / (2*a));
	if m > 0:
		return n + math.sqrt(m)/ (2*a),n - math.sqrt(m)/ (2*a)
	elif m == 0:
		return n
	if m < 0:
		return str(n) + "+" + str(math.sqrt(-m)/ (2*a)) + "i",str(n)+"-" +  str(math.sqrt(-m)/ (2*a))+"i";

print(quadratic(3,1,1))
print(quadratic(1,2,1))
print(quadratic(3,4,1))