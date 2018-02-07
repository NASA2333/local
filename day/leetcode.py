'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
Example:
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''


#解法一
'''
nums = [2, 7, 11, 15]
indexs =[]
list1 =[]
sum = int(input("请输入您的和"))
for index,num in enumerate(nums):
	indexs.append(index)

for i in range(len(nums)):
	for j in range(i+1,len(nums)):
		if nums[i]+nums[j] ==sum:
			list1.append(i)
			list1.append(j)
'''

#解法二
'''
nums = [2, 7, 11, 15]
sum = int(input("请输入您的和"))
for index,num in enumerate(nums):
	second = sum-num
	if second in nums[index+1:]:
		i2 = nums[index+1:].index(second)+index+1
		print(index,i2)
'''


'''
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
'''
'''
while 1:
	try:
		num1 =int(input("请输入第一个三位整数："))
		num2 = int(input("请输入第二个三位整数"))
	except Exception as msg:
		print("对不起您的输入有误")
	else:
		if len(str(num1)) !=3 or len(str(num2))!=3:
			print("您输入的数字不为三位数")
		else:
			a = list(str(num1))
			b = list(str(num2))
			print(a[::-1],'+',b[::-1])
			print(list(str(num1+num2))[::-1])
			break
'''

'''
Given a string, find the length of the longest substring without repeating characters.
Examples:
Given "abcabcbb", the answer is "abc", which the length is 3.
Given "bbbbb", the answer is "b", with the length of 1.
Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring,
 "pwke" is a subsequence and not a substring.
'''
#解法一
'''
def longofstr(s):
	str_1 =list(set(s))
	str_2 = ''.join(str_1)
	print(len(str_2),str_2)
'''
#解法二
'''
def longofstr(s):
	str_2 = []
	[str_2.append(x) for x in s if x not in str_2]
	print(len(str_2),''.join(str_2))
longofstr('acfaefdcadasdd34dad34')

'''
"""
There are two sorted arrays nums1 and nums2 of size m and n respectively.
Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
Example 1:
nums1 = [1, 3]
nums2 = [2]
The median is 2.0
Example 2:
nums1 = [1, 2]
nums2 = [3, 4]
The median is (2 + 3)/2 = 2.5
"""
'''
def findminds(nums1,nums2):
	list1 = sorted(sorted((nums1+nums2),reverse=False))
	choice = divmod((len(list1)),2)
	if choice[1]==0:
		mind =(list1[choice[0]]+list1[choice[0]-1])/2
		return mind
	else:
		mind =list1[choice[0]]
		return mind
print(findminds([2,3,4,5,6,22,3],[6,6,7,33,3,52,9,1,8,20,15,21,30]))
print(findminds([1,2,3,4],[5]))
'''


'''
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.
Example:
Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example:
Input: "cbbd"
Output: "bb"
'''

#判断是不是回文字符串
'''
def ispalindrom(s):
	lens = len(s)
	if lens <=1:
		return True
	L,r = 0,lens-1
	while L<r:
		if s[L] !=s[r]:
			return False
		L +=1
		r -=1
	return True

print(ispalindrom('abcddcba'))
'''

#感觉太精妙了
'''
def longpalinrome(s):
	lens = len(s)
	list = []
	for i in range(lens+1):
		for j in range(i,lens+1):
			if s[i:j] ==s[i:j][::-1]:
				list.append(s[i:j])
	b = max(list,key=len)
	print(list)
	return b
print(longpalinrome('cbababcdcbababc'))
# for i in range(len('cbababcdcbababc')):
# 	print(i)
# print(range(len('cbababcdcbababc')))
#
# print('cbababcdcbababc'[0:14])
# print('cbababcdcbababc'[0:14][::-1])
'''
'''
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
(you may want to display this pattern in a fixed font for better legibility)
P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:
string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".
'''

###这个题目有点莫名奇妙，不知道意义在哪


'''
Reverse digits of an integer.
Example1: x = 123, return 321
Example2: x = -123, return -321
click to show spoilers.
Note:
The input is assumed to be a 32-bit signed integer. Your function should return 0 when the reversed integer overflows.
'''
#如果需要保留个位数为0反之保留0的情况，讲处理成str，反之转换成int
'''
def reverse(d):
	if d>=0:
		return (str(d)[::-1])
	else:
		d_1 = abs(d)
		return (-(int(str(d_1)[::-1])))
print(reverse(10))
'''



'''
Implement atoi to convert a string to an integer.
Hint: Carefully consider all possible input cases. If you want a challenge,
 please do not see below and ask yourself what are the possible input cases.
Notes: It is intended for this problem to be specified vaguely (ie, no given input specs).
 You are responsible to gather all the input requirements up front.
'''
'''
def myAtoi(s):
	try:
		d =  int(float(s))
	except Exception as msg:
		return  False
	else:
		return d
print(myAtoi(18))
'''

'''Determine whether an integer is a palindrome. Do this without extra space.'''
#判断一个整数是否是回文数
'''
def ispalindrome(d):
	if str(d) ==str(d)[::-1]:
		return True
	else:
		return False
print(ispalindrome(1211))
'''

'''		Implement regular expression matching with support for '.' and '*'.		'''
'''
def isMatch(s,p):
	if s ==p:
		return True
	else:
		if len(p)>=2 and p[1]!='*':
			return False
'''
'''
def isMatch(text,pattern):
	if not pattern:
		return not text
	first_match = bool(text) and pattern[0] in {text[0],'.'}
	if len(pattern)>=2 and pattern[1]=='*':
		return  (isMatch(text,pattern[2:])) or first_match and isMatch(text[1:],pattern)
	else:
		return first_match and isMatch(text[1:],pattern[1:])

print(isMatch('aab','c*a*b'))
print("c*a*b".split('*'))
'''

'''
Given an integer, convert it to a roman numeral.
Input is guaranteed to be within the range from 1 to 3999.
罗马数字共有7个，即Ⅰ（1）、Ⅴ（5）、Ⅹ（10）、Ⅼ（50）、Ⅽ（100）、Ⅾ（500）和Ⅿ（1000）。
'''
'''
def intToRoman(num):
	c = [['','I','II','III','IV','V','VI','VII','VIII','IX'],['','X','XX','XXX','XL','L','LX','LXX','LXXX','XC'],
		 ['','C','CC','CCC','CD','D','DC','DCC','DCCC','CM'],['','M','MM','MMM']]
	s = []
	s.append(c[3][num//1000])
	s.append(c[2][num//100%10])
	s.append(c[1][num//10%10])
	s.append(c[0][num%10])
	print(''.join(s))

intToRoman(1986)
'''
'''
Given a roman numeral, convert it to an integer.
Input is guaranteed to be within the range from 1 to 3999.
'''
#罗马数字转成数字
'''
c = [['','I','II','III','IV','V','VI','VII','VIII','IX'],['','X','XX','XXX','XL','L','LX','LXX','LXXX','XC'],
	['','C','CC','CCC','CD','D','DC','DCC','DCCC','DM'],['','M','MM','MMM']]

def intToRoman(num):
	c = [['','I','II','III','IV','V','VI','VII','VIII','IX'],['','X','XX','XXX','XL','L','LX','LXX','LXXX','XC'],
		 ['','C','CC','CCC','CD','D','DC','DCC','DCCC','CM'],['','M','MM','MMM']]
	for i in range(4001):
		s = []
		s.append(c[3][i//1000])
		s.append(c[2][i//100%10])
		s.append(c[1][i//10%10])
		s.append(c[0][i%10])
		b = ''.join(s)
		if num ==b:
			print("这个数字是:",i)
			break
		else:
			s.clear()

intToRoman("MMMCDXCVI")
'''

'''
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0?
 Find all unique triplets in the array which gives the sum of zero.
Note: The solution set must not contain duplicate triplets.
For example, given array S = [-1, 0, 1, 2, -1, -4],
A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''
'''
def Solution(list):
	lsit = []
	bigList = sorted(list)
	# list_1 =[]
	for i in range(len(bigList)):
		for j in range(i+1,len(bigList)):
			for k in range(j+1,len(bigList)):
				if bigList[i]+bigList[j]+bigList[k] ==0:
					lsit.append([bigList[i],bigList[j],bigList[k]])
	# print(lsit)

	for i in lsit:
		for j in range(lsit.index(i)+1,len(lsit)):
			if i ==lsit[j]:
				del lsit[lsit.index(i)]
			break
	print(lsit)
Solution([-1, 0, 1, 2, -1, -4,2])

'''

'''
Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target.
Return the sum of the three integers. You may assume that each input would have exactly one solution.
 For example, given array S = {-1 2 1 -4}, and target = 1.
 The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
'''
#给定一个list，然后输入一个整数，从list取三个数相加，要求和与输入的数最相近
'''
#有点误解，留给以后思考吧
import itertools
def threeSumClosest(target,lsit):
	sumlist = []
	list_1 =list(itertools.permutations(lsit,3))

	# print(sum(list_1[0]))
	for i in list_1:
		gap = sum(i)+target
		sumlist.append([list_1.index(i),gap])
	targetlist = [len(sumlist),target]
	sumlist.append(targetlist)
	sum_list2=sorted(sumlist,key=lambda  x:x[1])
	index1 =sum_list2.index(targetlist)
	# if sum_list2[(index1-1)][1]-sum_list2[index1][1]
	print(list_1[23])

threeSumClosest(1,[-1,2,1,-4])
# print(type(sum((1,2,3))))
# a = [(1,2),(3,4)]
# print(sum(a[1]))
'''