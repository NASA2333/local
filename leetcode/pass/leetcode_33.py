'''
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
You are given a target value to search. If found in the array return its index, otherwise return -1.
You may assume no duplicate exists in the array.
'''
def search(nums,target):
	left =0
	right = len(nums)-1
	while left <=right:
		mid = left+(right-left)//2
		if nums[min] ==target:
			return  mid

		if nums[mid]>nums[left]:
			if nums[left] <=target <=nums[mid]:
				right =mid-1
			else:
				left = mid+1

		elif nums[mid]<nums[left]:
			if nums[mid]<=target<=nums[right]:
				left = mid+1
			else:
				right = mid-1
		else:
			left +=1
	return -1