'''
You are given a string, s, and a list of words, words, that are all of the same length.
Find all starting indices of substring(s) in s that is a concatenation of each word in
words exactly once and without any intervening characters.
For example, given:
s: "barfoothefoobarman"
words: ["foo", "bar"]
You should return the indices: [0,9].
(order does not matter).
'''
'''
s = "barfoothefoobarman"
a = ['foo']
if a[0] in s:
	print(s.index(a[0]))
	print(s.count(a[0]))
'''
def findSubstring(s,l):
	list1 = []
	for i in range(len(l)):
		counts = s.count(l[i])
		if counts ==0:
			list1.append('Null')
		elif counts ==1:
			list1.append(s.index(s[i]))
		else:
			for j in range(counts):
				list1.append(s.index(s[i]))
	return  list1
print(findSubstring("barfoothefoobarman",["foo", "bar",'data']))