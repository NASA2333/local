'''
Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

For example,
If nums = [1,2,2], a solution is:

[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
'''


from itertools import permutations
l =[]
def subsetsWithDup(s):
	for i in range(len(s)+1):
		l.append(list(permutations(s,i)))
	for i in l[1:]:
		l[0].extend(i)

	l2 = [sorted(list(i)) for i in l[0]]
	for i in range(len(l2)):
		if l2[i] in l2[i+1:]:
			l2[i] ="*"

	return [i for i in l2 if i !='*']

print(subsetsWithDup([1,2,2]))