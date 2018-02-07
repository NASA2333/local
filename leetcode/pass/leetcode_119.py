'''
Given an index k, return the kth row of the Pascal's triangle.
For example, given k = 3,
Return [1,3,3,1].

Note:
Could you optimize your algorithm to use only O(k) extra space?
返回杨辉三角指定行
'''
class getpascal():
	def pascal(self):
		a =[1]
		while 1:
			yield a
			a = [sum(i) for i in zip([0]+a,a+[0])]
	def getlist(self,t):
		n = 0
		for i in self.pascal():
			if n ==t-1:
				print(i)
				break
			else:
				n +=1
getpascal().getlist(5)




