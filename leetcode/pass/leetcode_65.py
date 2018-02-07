'''
Validate if a given string is numeric.
Some examples:
Some examples:
"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true
'''

def isnumber(s):
	try:
		s1 = eval(s)
	except Exception as msg:
		return False
	else:
		if isinstance(s1,int) or isinstance(s1,float):
			return True
		else:
			return False
print(isnumber('1L'))





