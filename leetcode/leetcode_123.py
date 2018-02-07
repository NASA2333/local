'''
Say you have an array for which the ith element is the price of a given stock on day i.
Design an algorithm to find the maximum profit. You may complete at most two transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
'''


###还有问题

a =[2, 4, 6, 1, 3, 8, 3,15]
def maxProfit(s):
	L=[]
	c=0
	j =0
	for i in range(1,len(s)):
		if s[i]>s[i-1]:
			c = s[i]

		else:
			if s[j:i-1]:
				L.append(c-min(s[j:i-1]))
				j =i
			else:
				pass
	if len(L)>=2:
		return  sum(sorted(L,reverse=True)[:2])

	else:
		return sum(L)

print(maxProfit(a))
