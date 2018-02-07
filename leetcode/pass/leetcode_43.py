'''
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2.
Note:
The length of both num1 and num2 is < 110.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
'''
def multiply(num1,num2):
	num1 = num1[::-1]
	num2 = num2[::-1]
	length1 = len(num1)
	length2 = len(num2)
	list1 = [0 for _ in range(len(num1)+len(num2)) ]
	for i in range(length1):
		for j in range(length2):
			list1[i+j] += int(num1[i]) * int(num2[j])

	choice = divmod(0,10)
	for i in range(len(list1)):
		num = choice[0]+list1[i]
		choice = divmod(num,10)
		list1[i] =choice[1]
	print(list1)

	sum =0
	for i in range(1,len(list1)+1):
		sum +=list1[i-1]*(10**(i-1))

	print(sum)
multiply('12345','56789')
