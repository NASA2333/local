'''
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.
'''

def setzeros(matix):
	c = [0 in i for i in matix]
	z=0
	for j in [0 in i for i in matix]:
		if j:
			for x in matix[c.index(j)]:
				if x ==0:
					z  = matix[c.index(j)].index(x)

	for i in range(len(matix)):			#分割
		if  0 in matix[i]:
			for z in range(len(matix[i])):
				matix[i][z] =0
		else:
			for j in range(len(matix[i])):
				if j ==z:
					matix[i][j] =0
	return matix

print(setzeros([[1,2,3,4],[4,0,6,4],[1,3,5,0]]))



# a= [[1,2,3],[4,5,6],[1,3,0]]
# c =[0 in i for i in a]
# z=0
# for j in [0 in i for i in a]:
# 	if j:
# 		for x in a[c.index(j)]:
# 			if x ==0:
# 				z  = a[c.index(j)].index(x)
#
# for i in range(len(a)):			#分割
# 	if  0 in a[i]:
# 		for z in range(len(a[i])):
# 			a[i][z] =0
# 	else:
# 		for j in range(len(a[i])):
# 			if j ==z:
# 				a[i][j] =0
# print(a)






# for i in

s = 'hello word'
print(s.split())
print(s.capitalize())
print([i.capitalize() for i in s.split()])