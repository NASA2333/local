import random
import re
for z in range(1000):
	b=[]
	for i in range(7):
		a= random.randint(0,9)
		b.append(a)

	sum= (b[0]*8+b[1]*7+b[2]*6+b[3]*5+b[4]*4+b[5]*3+b[6]*2)%11
	listnum = 11-sum
	if listnum ==10:
		b.append('X')
	elif listnum==11:
		b.append(0)
	else:
		b.append(listnum)

	b.insert(4,'-')
	issn ="".join(map(str,b))
	# print(issn)




	book = open(r"E:\issn.txt",'a')
	book.write(issn+"\n")
	book.close()
	b.clear()