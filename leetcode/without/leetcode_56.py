#Merge Intervals
'''
Given a collection of intervals, merge all overlapping intervals.
For example,
Given [1,3],[2,6],[8,10],[15,18],
return [1,6],[8,10],[15,18].
'''
#合并
def merge(L):
	a= []
	c =0
	# list1 =[]
	while 1:
		L1 =sorted(L,key=lambda x:x[0] )
		for i in range(len(L1)-1):
			if L1[i] in a:
				pass
			elif L1[i][1]>=L1[i+1][0]:
				if L1[i][0]>=L1[i+1][0] and L1[i][1]>=L1[i+1][1]:
					del L1[i+1]
					L = L1
				else:
					L1[i][1] =max(L1[i][1],L1[i+1][1])
					a.append(L1[i])
					del L1[i+1]
					L = L1
					break
			else:
				# if i ==len(L1)-1:
				# 	a.append(L1[i])
				# 	a.append(L1[i+1])

				# else:
				a.append(L1[i+1])
				# Z =  L1[i+1][1]
				# Z2 =L1[::-1][1]
				if L1[i+1][1] ==L1[-1][1]:
					c= len(L)
					# break
					return a

		# c+=1
		# if c >=len(L):
		# 	return a














	# for i in L1[:(len(L1)-1)]:
	# 	if i[1] >=L1[L1.index(i)+1][0]:
	# 		i[1] =max(i[1],L1[L1.index(i)+1][1])
	# 		# print(L)
	# 		a.append(i)
	# 		del L1[L1.index(i)+1]
	# 		# L = L
	# 		# list1.append(a)
	# 	else:
	# 		a.append(i)
	# 		# list1.append(a)
	#
	# return a

print(merge([[1,3],[8,10],[2,6],[15,18],[14,20]]))

# l = [[2,6],[1,3],[0,10],[15,18]]
# z = sorted(l,key=lambda x:x[0] )
# print(z)


# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e
#
#     # To print the result
#     def __str__(self):
#         return "[" + str(self.start) + "," + str(self.end) + "]"
#
#
# class Solution(object):
#     def merge(self, intervals):
#         """
#         :type intervals: List[Interval]
#         :rtype: List[Interval]
#         """
#         result = []
#         if not intervals:
#             return result
#         intervals.sort(key=lambda x: x.start)
#         result.append(intervals[0])
#         for interval in intervals[1:]:
#             prev = result[-1]
#             if prev.end >= interval.start:
#                 prev.end = max(prev.end, interval.end)
#             else:
#                 result.append(interval)
#         return result
#
#
# if __name__ == "__main__":
#     intervals = Solution().merge([Interval(1, 3), Interval(2, 6), Interval(8, 10), Interval(15, 18)])
#     for interval in intervals:
#         print(interval)


