import random

for j in range(1000):
	isbn_1 = []
	for i in range(9):
		a = random.randint(0,9)
		isbn_1.append(a)
	isbn_0 = random.choice([978,979])
	isbn_1.insert(0,isbn_0)
	sum_even = (int(isbn_1[0]/10)%10+isbn_1[1]+isbn_1[3]+isbn_1[5]+isbn_1[7]+isbn_1[9])*3
	sum_odd =(int(isbn_1[0]/1)%10+int(isbn_1[0]/100)%10+isbn_1[2]+isbn_1[4]+isbn_1[6]+isbn_1[8])
	check = 10-((sum_even+sum_odd)%10)
	if check ==10:
		isbn_1.append(0)
	else:
		isbn_1.append(check)
	isbn_1.insert(1,'-')
	isbn_1.insert(3,'-')
	isbn_1.insert(8,'-')
	isbn_1.insert(13,'-')
	# print(isbn_1)
	isbn = "".join(map(str,isbn_1))

	isbn_path = open(r'E:\isbn.txt','a')
	isbn_path.write(isbn+'\n')
	isbn_path.close()
	isbn_1.clear()



# sum = isbn_1[0]*10+isbn_1[1]*9+isbn_1[2]*8+isbn_1[3]*7+isbn_1[4]*6+isbn_1[5]*5+isbn_1[6]*4+isbn_1[7]*3+isbn_1[8]*2
# sub = 11-(sum%11)
# if sub ==11:
# 	isbn_1.append(0)
# elif sub ==10:
# 	isbn_1.append('x')
# else:
# 	isbn_1.append(sub)
# sum_even = (int(979/10)%10+8+7+8+7+0)*3
# sum_odd =(int(979/1)%10+int(979/100)%10+1+7+0+3)
# print(sum_even,sum_odd)
# print(str(isbn_1[0])[])
