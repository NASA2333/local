def tt(n):
	result =[]
	generate(n,n,'',result)
	return result
def generate(left,right,str,result):
	if left ==0 and right ==0:
		result.append(str)
	if left >0:
		generate(left-1,right,str+'(',result)
	if right >left:
		generate(left,right-1,str+')',result)
print(tt(3))