'''
Find the contiguous subarray within an array (containing at least one number) which has the largest sum.
For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
the contiguous subarray [4,-1,2,1] has the largest sum = 6.
'''
# list1 =[-2,1,-3,4,-1,2,1,-5,4]
class MaxSubArry():
	list2 =[]
	list1 =[-2,1,-3,4,-1,2,1,-5,4]
	def getap(self,l):
		for i in range(1,len(l)+1):
			self.list2.append(l[:i])

	def getlist(self,l1):
		for i in range(len(l1)):
			self.getap(l1[i:])
		z = ([sum(i) for i in self.list2])
		return self.list2[z.index(max(z))]

print(MaxSubArry().getlist([-2,1,-3,4,-1,2,1,-5,4]))


