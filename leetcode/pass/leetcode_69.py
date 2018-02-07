'''
Implement int sqrt(int x).
Compute and return the square root of x.
x is guaranteed to be a non-negative integer.
'''
#用除法求根

def getsqtr(s):
	for i in range(int(s/2)+1):
		if i*i <=s and (i+1)*(i+1) >s:
			return  i

print(getsqtr(24))