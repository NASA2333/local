'''
Given a sorted array and a target value, return the index if the target is found. If not,
return the index where it would be if it were inserted in order.
You may assume no duplicates in the array.
Here are few examples.
[1,3,5,6], 5 → 2
[1,3,5,6], 2 → 1
[1,3,5,6], 7 → 4
[1,3,5,6], 0 → 0
'''

def searchInsert(nums,target):
	if target in nums:
		return nums.index(target)
	else:
		if target <nums[0]:
			return 0
		elif target >nums[-1]:
			return len(nums)
		else:
			for i in range(0,len(nums)-1):
				if nums[i] <=target <=nums[i+1]:
					return  i+1


print(searchInsert([1,3,5,6],3))