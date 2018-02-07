'''
Given an array of non-negative integers, you are initially positioned at the first index of the array.
Each element in the array represents your maximum jump length at that position.
Your goal is to reach the last index in the minimum number of jumps.
For example:
Given array A = [2,3,1,1,4]
The minimum number of jumps to reach the last index is 2. (Jump 1 step from index 0 to 1, then 3 steps to the last index.)
Note:
You can assume that you can always reach the last index.
'''

def jump(s):

	b = 0
	for i in range(len(s)):
		sum = 0
		sum = i+s[i]
		if sum ==len(s)-1:
			# print(b)
			b +=1
			return b
			# break
		else:
			b +=1


print(jump([2,1,2,1,4]))