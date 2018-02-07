'''
Reverse a linked list from position m to n. Do it in-place and in one-pass.

For example:
Given 1->2->3->4->5->NULL, m = 2 and n = 4,

return 1->4->3->2->5->NULL.

Note:
Given m, n satisfy the following condition:
1 ≤ m ≤ n ≤ length of list.
'''

def reverseBetween(s,m,n):
	s[m-1],s[n-1] =s[n-1],s[m-1]
	return s

print(reverseBetween([1,2,3,4,5],2,4))