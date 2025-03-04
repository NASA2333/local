'''
You are climbing a stair case. It takes n steps to reach to the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
Note: Given n will be a positive integer.
Example 1:
Input: 2
Output:  2
Explanation:  There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:
Input: 3
Output:  3
Explanation:  There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
'''




#每次1或2 求总共方案(斐波那契）
def climbstairs(s):
	if s <=2 :
		return s

	dp = [0 for _ in range(s)]
	dp[0] =1
	dp[1] =2
	# print(dp)
	for i in range(2,s):
		dp[i] = dp[i-1]+dp[i-2]
	return dp[s-1]

print(climbstairs(8))
