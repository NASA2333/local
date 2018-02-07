'''
Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.
For example, given the following matrix:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0
Return 6.
'''

def maxmalRectangle(s):
	s1 = [sum(i) for i in list(zip(*s))]
	s1.insert(0,0)
	return s1


print(maxmalRectangle([[1,0,1,0,0],[1,0,1,1,1],[1,1,1,1,1],[1,0,0,1,0]]))














# a = [[1,0,1,0,0],[1,0,1,1,1],[1,1,1,1,1],[1,0,0,1,0]]

# for i in a:
# 	# print(list(zip(i)))

# print(list(zip(*a)))

# print(list(zip([j for i in a for j in i])))

# l =[]
# sum0 =0
# for i in a:
# 	sum0 +=i[0]
# l.append(sum0)
# print(l)

# for i in range(len(a[0])):
# 	pass
# for i in range(len(a)):
# 	sum+str(i) =







# b = [1,0,1,0,0]
# c =[1,0,1,1,1]
# d =[1,1,1,1,1]
# e =[1,0,0,1,0]
# f = [i for i in a]
# g = [zip(i) for i in a]
# print(f)
# for i in g:
# 	print(i)
# print(list(zip(b,c,d,e)))
#
# print([zip(i) for i in a])