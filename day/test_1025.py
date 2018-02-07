#遍历系统文件

import os

l = []
def listdir(xpath):
	for i in os.listdir(xpath):
		if os.path.isdir(os.path.join(xpath,i)):
			listdir(os.path.join(xpath,i))
		else:
			l.append(os.path.join(xpath,i))
			# print(os.path.join(xpath,i))

listdir(r'D:\python')
print(len(l))
print(l)
print(os.path.join(r"D:\python",'text.txt'))
z =['yy']
print(bool(z))
# for i,j,y in os.walk(r'D:\python'):
# 	print(i)

ll = [1,2,3,4]
# ll.append("a",'bb')
ll.extend(['bbccc'])
print(ll)