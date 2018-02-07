#冒泡序列
import time
a = time.clock()
numlist = [1,4,5,6,1,2,4,5,78,7,9,14,56,54,3,4]

for j in range(len(numlist)-1):
	for i in range(len(numlist)-j-1):
		if numlist[i]>numlist[i+1]:
			numlist[i],numlist[i+1]=numlist[i+1],numlist[i]
print(numlist)
print(time.clock())