'''
Given a linked list, swap every two adjacent nodes and return its head.
For example,
Given 1->2->3->4, you should return the list as 2->1->4->3.
Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be changed.
'''

def swapPairs(head):
	for i in range(len(head)):
		if i%2 ==0:
			if i+1 >=len(head):
				pass
			else:
				head[i],head[i+1] =head[i+1],head[i]
	return  head

print(swapPairs([1,2,3,4,5,6,7]))



