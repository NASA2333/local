'''
Given two words word1 and word2, find the minimum number of steps required to convert word1 to word2. (each operation is counted as 1 step.)
You have the following 3 operations permitted on a word:
a) Insert a character
b) Delete a character
c) Replace a character
'''
#递推表达式，不会写
#len ==  ---替换  len >   删除   len <插入


def minDistance(s1,s2):
	sum = 0
	if len(s1) ==len(s2):
		for i in range(len(s1)):
			if s1[i] !=s2[i]:
				sum +=1
		return sum
	elif len(s1) < len(s2):
		for i in s1:
			if i in s2:
				if len(s2[s2.index(i):]) >len(s1[s1.index(i):]):
					sum -=1


print(minDistance('acc','aba'))