'''
Given an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent,
 with the colors in the order red, white and blue.
Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note:You are not suppose to use the library's sort function for this problem.
尽量只是用一次循环，不适用排序，将列表中相同的的元素放在一起
输入: nums = [1, 2, 1, 2, 0, 2, 1, 0, 2, 0, 0, 2]
输出: [0, 0, 0, 0, 1, 1, 1, 2, 2, 2, 2, 2]
'''

##insert 索引不可以为负数


def sortColors(nums):
	L = len(nums)
	sum1 = 0
	while sum1 <=L:
		if nums[sum1] ==0:
			nums.insert(0,0)
			del nums[sum1+1]
			sum1 +=1
		elif nums[sum1] ==2:
			nums.extend([2])
			del nums[sum1]
			L -=1
		else:
			sum1 +=1
	return nums
print(sortColors([1, 2, 1, 2, 0, 2, 1, 0, 2, 0, 0, 2,1,2,1,1,1,0,1,2,0]))




