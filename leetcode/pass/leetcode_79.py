'''
Given a 2D board and a word, find if the word exists in the grid.
The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally
or vertically neighboring. The same letter cell may not be used more than once.
For example,
Given board =

[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
word = "ABCCED", -> returns true,
word = "SEE", -> returns true,
word = "ABCB", -> returns false.
'''


def  exist(s,t):
	# for i in t:
	# 	if t.count(i) >s.count(i):
	# 		return False

	s1 = []
	for i in s:
		s1.extend(i)

	for z in t:
		for j in range(len(s1)):
			if z ==s1[j]:
				s1[j] ='*'
				break
	if s1.count('*') ==len(t):
		return True
	else:
		return False

print(exist([
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
],'ABCB'))




