'''
Divide two integers without using multiplication, division and mod operator.
If it is overflow, return MAX_INT.
'''
'''
def divide(n,m):
	i =0
	c = abs(n)-abs(m)
	b =[]
	while 1:
		if c >=0:
			i +=1
			c = c-abs(m)
		else:
			j = abs(m)-abs(c)
			break
	if n <0 or m<0:
		i = -i
		j =-j
		b.append(i)
		b.append(-j)
	else:
		b.append(i)
		b.append(j)
	return  b

print(divide(-5,-2))
print(divmod(-5,-2))
print(divmod(5,2))
'''
#按照减法运算来计算，会出现点问题，解法涉及到位运算，有点懵逼
class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        MAX_INT = 2147483647
        sign = 1
        if dividend >= 0 and divisor < 0 or dividend <= 0 and divisor > 0:
            sign = -1
        dividend = abs(dividend)
        divisor = abs(divisor)

        result = 0
        current = divisor
        currentResult = 1
        while current <= dividend:
            current <<= 1
            currentResult <<= 1
        while divisor <= dividend:
            current >>= 1
            currentResult >>= 1
            if current <= dividend:
                dividend -= current
                result += currentResult
        return min(sign * result, MAX_INT)


if __name__ == "__main__":
    assert Solution().divide(5, -1) == -5
    assert Solution().divide(10, 2) == 5