#jump game
'''
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

For example:
A = [2,3,1,1,4], return true.

A = [3,2,1,0,4], return false.
'''

def canjump(L):
	index =0
	for i in range(len(L)):
		try:
			index = index+L[index]
		except Exception as msg:
			return False
		if index ==len(L)-1:
			return True
		else:
			pass
	else:
		return False
print(canjump([1,2,2,2,1,1]))


