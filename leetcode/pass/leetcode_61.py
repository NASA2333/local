'''
Given a list, rotate the list to the right by k places, where k is non-negative.

Example:
Given 1->2->3->4->5->NULL and k = 2,

return 4->5->1->2->3->NULL.
'''
#
a= [1,2,3,4,5,6,7]
# print(a[-4:-1])
# print(a[-3])
# print(a.index(3))
# del a[0]
# a.insert(0,[5,6,7])
# print(a)

def rotateRight(head,k):
	c = head[-(k+1):-1]
	index1 = head.index(c[-1])
	for i in c[::-1]:
		del head[index1]
		head.insert(0,i)
	return head
print(rotateRight([1,2,3,4,5,6],3))
