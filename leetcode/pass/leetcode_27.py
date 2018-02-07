'''
Given an array and a value, remove all instances of that value in place and return the new length.
Do not allocate extra space for another array, you must do this in place with constant memory.
The order of elements can be changed. It doesn't matter what you leave beyond the new length.
Example:
Given input array nums = [3,2,2,3], val = 3
Your function should return length = 2, with the first two elements of nums being 2.
'''

def removeElement(nums,val):
	# list_1 = set(nums)
	# for i in list(list_1):
	# 	if i ==val:
	# 		list_1.remove(i)
	# return list(list_1)
	'''
	b = []
	for i in nums:
		if i != val:
			b.append(i)
		else:
			pass
	return b
	'''
	return [i for i in nums if i !=val]
print(removeElement([1,2,3,1,2,2,5,5,5,5,555],2))
'''
这种方法还要好些问题
for i in range(len(nums)):
		if nums[i] ==val:
			nums[i]=''
			# removeElement(nums,val)
	for i in nums:
		if i =='':
			nums.remove(i)
	return nums
	'''