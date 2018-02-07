'''
Given an unsorted integer array, find the first missing positive integer.
For example,
Given [1,2,0] return 3,
and [3,4,-1,1] return 2.
Your algorithm should run in O(n) time and uses constant space.
'''
def firstMissingPostitive(nums):
	b = sorted(nums)
	c = b[0]+1
	while 1:
		if c <=0:
			c +=1
		else:
			if c not in b:
				return c
			else:
				c+=1

print(firstMissingPostitive([3,4,-1,1]))