'''
The gray code is a binary numeral system where two successive values differ in only one bit.
Given a non-negative integer n representing the total number of bits in the code, print the sequence of gray code.
A gray code sequence must begin with 0.

For example, given n = 2, return [0,1,3,2]. Its gray code sequence is:

00 - 0
01 - 1
11 - 3
10 - 2
'''


def grayCode( n):
        """
        :type n: int
        :rtype: List[int]
        """
        result = [(i >> 1) ^ i for i in range(pow(2, n))]
        return result


print(grayCode(2))
# # print(pow(2, 2))
# print(3 >> 1)