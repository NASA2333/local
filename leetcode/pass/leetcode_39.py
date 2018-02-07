'''
Given a set of candidate numbers (C) (without duplicates) and a target number (T),
find all unique combinations in C where the candidate numbers sums to T.
The same repeated number may be chosen from C unlimited number of times.
Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
For example, given candidate set [2, 3, 6, 7] and target 7,
A solution set is:
[
  [7],
  [2, 2, 3]
]
'''

#从集合中选择出和为target的数字组合，组合不能重复，数字可以重复使用
from itertools import product
def combinationSum(candidates,target):
	a = []
	b= []
	c = []
	for i in range(1,target):
		a.append(list(product(candidates,repeat=i)))
	for j in a:
		for x in j:
			if sum(x) ==target:
				b.append(x)

	for i in b:
		tu = sorted(list(i))
		c.append(tuple(tu))

	return set(tuple(c))


print(combinationSum([2, 3, 6, 7],9))

