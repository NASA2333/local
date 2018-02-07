#给定一个集合，得出所有子集，子集包含子集及空集

from itertools import permutations

def getlist(s):
	# L =[]
	# for i in range(len(s)+1):
	# 	L.extend(list(permutations(s,i)))
	# print(type(L[1]))
	# return L
	# print(L[1])
	result = [[]]
	for num in sorted(s):
		result += [item + [num] for item in result]
	return result

print(getlist([1,2,3,4]))