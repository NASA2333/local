# # a= [ i for i in range(10)]
# # print(a)
# # print(type(a))
# # for i in range(10):
# # 	pass
# # c =iter( 'hello')
# # print(next(c))
# # print(type(c))
# l = [x for x in range(10)]
# print(type(l))
# s = (x for x in range(10))
# print(type(s))
# print(next(s))
# print(next(s))
# print(next(s))
# print(next(s))
# # print(next(l))
# z =range(10)
# from collections import Iterator,Iterable
# print(isinstance([],Iterable))
# print(isinstance(range(10),Iterable))
# print(isinstance('123',Iterable))
# print(type(iter('abc')))


#假设要用50、20、10、5、1（元）找出87元来 make_change(87, [50,20,10,5,1)
class Getmoney():
	# count = 0
	def getmoney(self,money):
		self.count = 0
		if (divmod(money,50))[0]==0:
			self.getmoney20((divmod(money,50))[1])
			return self.count
		else:
			self.count +=(divmod(money,50))[0]
			self.getmoney20((divmod(money,50))[1])
			return self.count
	def getmoney20(self,money):
		if (divmod(money,20))[0]==0:
			self.getmoney10((divmod(money,20))[1])
		else:
			self.count +=(divmod(money,20))[0]
			self.getmoney10((divmod(money,20))[1])

	def getmoney10(self,money):
		if (divmod(money,10))[0]==0:
			self.getmoney5((divmod(money,10))[1])
		else:
			self.count +=(divmod(money,10))[0]
			self.getmoney5((divmod(money,10))[1])

	def getmoney5(self,money):
		if (divmod(money,5))[0]==0:
			self.getmoney1((divmod(money,5))[1])
		else:
			self.count +=(divmod(money,5))[0]
			self.getmoney1((divmod(money,5))[1])

	def getmoney1(self,money):
		self.count +=(divmod(money,1))[0]


# a = Getmoney()
# print(a.getmoney(13))

# l = [divmod(87,i)[0] for i in [50,20,10,5,1]]
# print(l)
# print(divmod(87-(l[0]*50),20))
l = []
def getmone(money):

	z = [50,20,10,5,1]
	for i in z:
		change = divmod(money,i)
		if change[1] ==0:
			l.append(change[0])
			break
		else:
			l.append(change[0])
			money = change[1]
	return l

# print(sum(getmone(80)))

# str = ' python str '
# print(str)
# print(str.strip())
# print(str.lstrip())
# print(str.rstrip())
# print(str.replace(" ",""))

# str = 'ab c\nde '
# print(str.splitlines())
# print(str.partition("\n"))
# print(str.split(' '))
# c = (1,2)
# print(type(c))
# a = [i for i in range(10)]
# b = (i for i in range(10))
# print(type(a))
# print(type(b))
# print(dir(a))
# print(dir(b))

def g():
	for i in range(10):
		yield i
		# print(x)

a = g()
# print(a.send(None))
# print(a.send('keji'))
# while 1:
# 	print(next(a))

li = (i for i in range(10))
print(type(li))
from collections import Iterator,Iterable
print(isinstance(li,Iterator))
print(isinstance(li,Iterable))
c = iter([1,2,3,4])


L = iter(range(20))
while 1:
	try:
		x = next(L)

	except StopIteration:
		break



import time,sys
time_start = time.time()
g1 = [x for x in range(10000000)]
time_end = time.time()
print("列表生成式耗时：",time_end-time_start)
print("列表生成式占用内存：",sys.getsizeof(g1))

time_start1 = time.time()
g2 = (x for x in range(10000000))
time_end1 =time.time()
print("生成器耗时：",time_end1-time_start1)
print("生成器占用内存：",sys.getsizeof(g2))