
'''
Implement int sqrt(int x).

Compute and return the square root of x.

x is guaranteed to be a non-negative integer.


'''
# import math
#
# print(int(math.sqrt(8)))

def mysqrt(x):
	for i in range(x//2+1):
		if i*i <x and ((i+1)*(i+1))>x:
			return i
		elif i* i ==x:
			return i

print(mysqrt(15))