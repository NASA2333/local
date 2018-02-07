'''
Given a collection of distinct numbers, return all possible permutations.
For example,
[1,2,3] have the following permutations:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
'''
from itertools import permutations

def permute(s):
	s= list(permutations(s))
	return s

print(permute([1,2,3]))