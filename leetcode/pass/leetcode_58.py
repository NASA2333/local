'''
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.
If the last word does not exist, return 0.
Note: A word is defined as a character sequence consists of non-space characters only.
'''

def lengofLastWord(s):
	try:
		s.split()[-1]
	except Exception as msg:
		return 0
	else:
		return len(s.split()[-1])

print(lengofLastWord("hello word"))