'''
Given a linked list, remove the nth node from the end of list and return its head.
For example,
   Given linked list: 1->2->3->4->5, and n = 2.
   After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:
Given n will always be valid.
Try to do this in one pass.
'''
def removeNthFromEnd(head,n):
	if n>len(head):
		print("对不起，超出范围")
	else:
		index = -n
		del head[index]
	return head

print(removeNthFromEnd(['a','b','c','d','e','f'],-1))