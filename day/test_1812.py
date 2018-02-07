import random,string,time,os,sys,random

# print(''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(2)))
# entityname1 = "测试数据"+str(int(time.time()))
# entityname2 = "测试数据"+str(int(time.time())+1)
#
# print(entityname1)
# print(entityname2)
file_path = os.path.abspath(r'.\date')
# print(file_path)
# print(sys.path)
b = ''.join([str(random.randint(0,9)) for i in range(6) ])

print(b)

a = ['1','2','1','4']
print(set(a))
for i in set(a):
	print(i)


a0 = dict(zip(('a','b','c','d','e'),(1,2,3,4,5)))		#字典
a1 = range(10)

a3 = []
for i in a0:
	a3.append(a0[i])

a4 = []

for i in a1:
	if i in a3:
		a4.append(i)

a5 = {}

for i in a1:
	a5[i] =i*i
print(a0,a1,a3,a4,a5)





