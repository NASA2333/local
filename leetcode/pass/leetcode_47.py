'''
Given a collection of numbers that might contain duplicates, return all possible unique permutations.
For example,
[1,1,2] have the following unique permutations:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
'''
from itertools import  permutations

def permuteUnique(s):
	s = list(permutations(s))
	return set(s)

print(permuteUnique([1,1,2]))