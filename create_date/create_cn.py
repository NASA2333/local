# import random
#
# for i in range(1000):
# 	a = []
# 	for i in range(6):
# 		a.append(random.randint(0,9))
# 	a.insert(2,'-')
# 	cn = "".join(map(str,a))
# 	# print(cn)
#
# 	b = open(r'E:\cn.txt','a')
# 	b.write(cn+'\n')
# 	b.close()
# 	a.clear()

#去除重复
b = open(r'E:\isbn.txt','r')
c = open(r'E:\isbn_1.txt','w')
a = []
for i in b:
	if i not in a:
		a.append(i)

for z in a:
	c.write(z)

c.close()
b.close()
