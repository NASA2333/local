'''
The set [1,2,3,…,n] contains a total of n! unique permutations.
By listing and labeling all of the permutations in order,
We get the following sequence (ie, for n = 3):
"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.
Note: Given n will be between 1 and 9 inclusive.
'''
from itertools import permutations
def getPermutation(n,k):
	list1 = list(permutations(range(1,n+1)))
	list2 =[]
	for i in list1:
		strs =''
		for j in i:
			strs +=str(j)
		list2.append(strs)
	try:
		k_num = (sorted(list2,reverse=True))[k-1]
	except Exception as msg:
		return False
	# print(list2)
	return k_num



print(getPermutation(6,3))

