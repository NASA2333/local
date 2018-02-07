'''
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.
给定一个m x n 的举证，当其中某一个元素为0时，将该行与该列的所有数据变为0
'''

def setZeroes(mattix):
	L=[]
	for index,i in enumerate(mattix):
		for index2,j in enumerate(i):
			if j ==0:
				L.append([index,index2])
	for i in L:
		for j in range(len(mattix[0])):
			mattix[j][i[1]] =0
			mattix[i[0]][j] =0
	print(L)
	return mattix






print(setZeroes([[1, 1, 1, 1],
[1, 1, 0, 1],
[1, 1, 1, 0],
[1, 1, 1, 1],
[0,1,1,1]]))