'''
Given two binary strings, return their sum (also a binary string).
For example,
a = "11"
b = "1"
Return "100".
'''

##二进制转换为十进制  int（x,2)   十进制转换成二进制  bin（）
def addBiary(a,b):
	sum = int(a,2)+int(b,2)
	return bin(sum)

print(addBiary('11','1')[2:])