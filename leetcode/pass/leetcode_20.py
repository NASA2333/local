'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
'''
def isVaild(s):
	a ='('+')'
	b = '['+']'
	c = '{'+'}'
	n = 0
	x = len(s)-1
	while 1:
		if n <=x:
			if s[n]+s[x] ==a or s[n]+s[x] ==b or s[n]+s[x] ==c:
				pass
			else:
				return False
		else:
			return  True
		n +=1
		x -=1

print(isVaild("([{[]}])"))
