'''
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).
For example,
S = "ADOBECODEBANC"
T = "ABC"
Minimum window is "BANC".

Note:
If there is no such window in S that covers all characters in T, return the empty string "".

If there are multiple such windows, you are guaranteed that there will always be only one unique minimum window in S.
'''

# def minwindow(s,t):
# 	l =[]
# 	for i in range(len(s)):
# 		for j in range(i+1,len(s)):
# 			for i in range(len(t)):
# 				if t[i] in
from  itertools import  combinations
from copy import  deepcopy

def getsmall(s,t):
	L=[]
	for i in range(len(t),len(s)+1):
		L.append(list(combinations(s,i)))
	L2=[]
	for j in L:
		zz =deepcopy(j)
		for z in j:
			for i in t:
				if i in z:
					pass
				else:
					zz.remove(z)
					break

		L2.append(zz)
	for i in L2[1:]:
		L2[0].extend(i)
	print(min(L2[0],key=len))

# getsmall("ADOBECODEBANC","ABC")


# l3 =[(1,2,3),(4,5)]
# del l3[0]
# print(l3)


s = "ADOBECODEBANC"
t = "ABC"

L=[]
for i in range(len(s)):
	for x in range(i,len(s)):
		l = s[i:x+1]
		L.append(l)
		for j in t:
			if j in l:
				pass
			else:
				L.remove(l)
				break
print(min(L,key=len))





