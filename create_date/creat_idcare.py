import random
for i in range(1001):
	Birthday =[]													#生日
	addrs =[str(random.choice(range(110000,999999))).zfill(6)]			#地区
	order = [str(random.choice(range(0,999))).zfill(3)]				#序列
	mult = [7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
	check = [1,0,'X',9,8,7,6,5,4,3,2]
	year = str(random.randint(1960,2017))
	month = str(random.choice(range(1,13))).zfill(2)

	if month ==2:
		days = random.choice(range(1,29))
		days = str(days).zfill(2)
	elif month in (1,3,5,7,8,10,12):
		days = str(random.choice(range(1,32))).zfill(2)
	else:
		days = str(random.choice(range(1,31))).zfill(2)

	Birthday.extend((year,month,days))
	list1 = addrs+Birthday+order
	list2 =''.join(list1)
	sum = 0
	for i in range(len(list2)):
		avg1 =int(list2[i])*mult[i]
		sum +=avg1
	mod = check[sum%11]

	xpath = open(r'E:\idcare.txt','a')
	xpath.write(list2+str(mod)+'\n')
