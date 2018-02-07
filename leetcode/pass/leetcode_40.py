'''
Given a collection of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.
Each number in C may only be used once in the combination.
Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
For example, given candidate set [10, 1, 2, 7, 6, 1, 5] and target 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
'''


from itertools import product
def combinationSum(candidates,target):
	a = []
	b= []
	c = []
	d =[]
	for i in range(1,target):
		a.append(list(product(candidates,repeat=i)))
	for j in a:
		for x in j:
			if sum(x) ==target:
				b.append(x)

	for i in b:
		tu = sorted(list(i))
		c.append(tuple(tu))

	for i in c:
		if len(i) ==len(set(i)):
			d.append(i)
	print(c)
	return set(tuple(d))


print(combinationSum([2, 3, 6, 7],9))