'''
Given a non-negative integer represented as a non-empty array of digits, plus one to the integer.
You may assume the integer do not contain any leading zero, except the number 0 itself.
The digits are stored such that the most significant digit is at the head of the list.
'''

def plusOne(dig):
	a = "".join(map(str,dig))
	c = list(str(int(a)+1))
	d = [int(i) for i in c]
	return d

print(plusOne([1,2,3,4,9]))