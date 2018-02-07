'''
Follow up for "Remove Duplicates":
What if duplicates are allowed at most twice?
For example,
Given sorted array nums = [1,1,1,2,2,3],
Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3.
 It doesn't matter what you leave beyond the new length.


'''

def removeDuplicates(s):
	for i in s:
		if s.count(i)>2:
			s.remove(i)
		else:
			pass
	return len(s),s
print(removeDuplicates([1,1,1,2,2,3]))