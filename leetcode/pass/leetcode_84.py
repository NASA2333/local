'''
Given a sorted linked list, delete all duplicates such that each element appear only once.
For example,
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3
'''


def deleteDuplicates(s):

	for i in range(len(s)):
		if  s[i] in s[i+1:]:
			s[i] ='*'

	return [i for i in s if i !='*']

print(deleteDuplicates([1,2,2,3,3,4]))

# a =[1,2,2,3,3,4]
# print(a[1:])
