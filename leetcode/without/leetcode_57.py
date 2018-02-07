'''
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).
You may assume that the intervals were initially sorted according to their start times.
Example 1:
Given intervals [1,3],[6,9], insert and merge [2,5] in as [1,5],[6,9].
Example 2:
Given [1,2],[3,5],[6,7],[8,10],[12,16], insert and merge [4,9] in as [1,2],[3,10],[12,16].
This is because the new interval [4,9] overlaps with [3,5],[6,7],[8,10].
'''

# def insert(inter,newinter):
# 	L = []
# 	for i in inter:
# 		a = range(i[0],i[1]+1)
# 		for index,j in iter(newinter):
# 			if j not in a:
# 				if index not in a:
# 					L.append(i)
# 			else:
# 				newinter =[min(newinter[0],i[0]),max(newinter[1],i[1])]
# 	return L
#
# print(insert(([1,2],[3,5],[6,7],[8,10],[12,16]),[4,9]))

print(4 in range(3,6))
		
