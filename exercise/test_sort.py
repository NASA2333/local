a =[1,2,3,4,5,6,7,8,9,10]
a.sort(reverse=True)
print(a)
b = sorted([1,2,3,4,5,6,7,8,9],reverse=True)
print(b)

list=[2,3,5,7,11,24,3,4,9,2,4,6,4,7,14,6]
for j in range(len(list)-1):
	for i in range(len(list)-1):
		if list[i]>list[i+1]:
			list[i],list[i+1] =list[i+1],list[i]
		else:
			pass

print(list)

a = input(u"中文")