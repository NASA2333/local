'''
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.
The number of elements initialized in nums1 and nums2 are m and n respectively.
'''

def merge(s1,s2):
	s1.extend(s2)
	return sorted(s1)


print(merge([1, 1, 2, 2, 4],[0, 0, 2, 3]))
