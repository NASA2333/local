'''
Merge two sorted linked lists and return it as a new list.
The new list should be made by splicing together the nodes of the first two lists.
'''
#list直接追加（extend())，如果需要在排序，则在sorted

def mergeTwoLists(l1,l2):
	l1.extend(l2)
	return sorted(l1,reverse=True)

print(mergeTwoLists([2,3,4,5,6],[7,3,5,7,6,3,2,1]))
