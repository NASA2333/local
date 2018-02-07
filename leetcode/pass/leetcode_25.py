'''
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.
k is a positive integer and is less than or equal to the length of the linked list.
 If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.
You may not alter the values in the nodes, only nodes itself may be changed.
Only constant memory is allowed.
For example,
Given this linked list: 1->2->3->4->5
For k = 2, you should return: 2->1->4->3->5
For k = 3, you should return: 3->2->1->4->5
'''
#按照k的倍数将head进行分割，在倍数内的数据进行倒序排列，不足倍数的保持顺序不变

def reverseKGroup(head,k):
	a = [head[i:i+k] for i in range(0,len(head),k)]
	for i in range(len(a)):
		if len(a[i]) <k:
			pass
		else:
			a[i] =a[i][::-1]
	b =[]
	for i in a:
		b.extend(i)
	return b
# b = [1,2,3,4,5]
# print([b[i:i+3] for i in range(0,len(b),3)])
# print(b[::-1])
print(reverseKGroup([1,2,3,4,5,6,7,8,9,10],4))


