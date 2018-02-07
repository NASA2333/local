'''
Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.

For example,
Given:
s1 = "aabcc",
s2 = "dbbca",

When s3 = "aadbbcbcac", return true.
When s3 = "aadbbbaccc", return false.
'''

def isInterlevae(s1,s2,s3):
	for i in s3:
		if s3.count(i) ==s2.count(i)+s1.count(i):
			return True
		else:
			return  False


print(isInterlevae("aabcc","dbbca","aadbbbaccc"))
