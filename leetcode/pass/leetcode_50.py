'''
Implement pow(x, n).
'''
# print(pow(10,4,3))

def getPow(l):
	if len(l) in (2,3):
		sum =l[0]
		for i in range(l[1]-1):
			sum = sum*l[0]

		if len(l) ==2:
			return sum
		else:
			return sum%l[2]

	else:
		return False

print(getPow([10,2,3]))