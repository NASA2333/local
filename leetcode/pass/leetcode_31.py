'''
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).
The replacement must be in-place, do not allocate extra memory.
Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
'''
import operator
def nextPermutation(nums):
	num = int(nums)
	# b = ''
	while 1:
		num +=1
		if sorted(str(num)) ==sorted(str(nums)):
			return num
			# break
		elif len(str(num))>len(str(nums)):
			return str(nums)[::-1]

print(nextPermutation(7654321))
# print(bool(dict(['a','b']) ==dict(['b','a'])))
# print(bool(set()))
# print(operator.eq('abc','bac'))
# b= [x for x in 'abc']
# print(b)
# print(str(123)[::-1])