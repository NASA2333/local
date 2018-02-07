'''
Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.
For example,
Given 1->2->3->3->4->4->5, return 1->2->5.
Given 1->1->1->2->3, return 2->3.
'''

def deleteDuplicates(s):
	dicts = {}
	for index,i in enumerate(s):
		if i in dicts:
			dicts[i].append(index)
		else:
			dicts[i] =[index]

	for i in dicts.values():
		if len(i)>=2:
			for j in i:
				s[j] =' '
	a =''.join([str(i) for i in s])
	return [ int(i) for i in list(a.replace(" ",""))]

print(deleteDuplicates([1,1,2,3,4,5,3,4]))