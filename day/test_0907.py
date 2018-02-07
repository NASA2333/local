#coding =utf-8
# def gg():
# 	yield 1
# 	yield 2
# 	yield 3
# c = gg()
# for i in range(3):
# 	print(next(c))
# # print(next(c))
# x = 4
# print(x*x)
# print(0%2)
# print(zip(['abc'],['cde']))

# class Iter:
#     def __init__(self):
#         self.start=-1
#     def __iter__(self):
#         return self
#     def __next__(self):
#         self.start +=2
#         return self.start
# I = Iter()
# for count in range(5):
#     print(next(I))

# def add():
# 	a = [1,2,3,4,5]
# 	return a
#
# print(add()[1])

# from test import test_0911
#
# key = test_0911.main()
# # keys = test_0911.onKeyboardEvent
#
# # if key =="Y":
# # 	print("yes")
# print(key)

# a= ['a','b','c','d']
# print(type(a))
#
# for index,i in enumerate(a):
# 	print(i,index)
#
# class test():
# 	def add(self):
#
# 		self.c = a+b
# import copy
# service_list = open(r"D:\python\study\data\day3\bank_balance.txt",'r',encoding='utf-8').readlines()
# l = copy.deepcopy(service_list)
# # del service_list[1]
# ser = open(r"D:\python\study\data\day3\bank_balance.txt",'w',encoding='utf-8')
# for i in l:
# 	line = i.split()
# 	if line[0] =="华夏":
# 		pass
# 	else:
# 		ser.write(i+'\n')
# ser.close()
# print(l)
# # print(service_list)
# for index,i in enumerate(service_list,1):
# 	print(index,i)
# print(service_list)
# for i in service_list:
# 	line = i.split()
# 	if i[1] ==

#
# with open(r"D:\python\study\data\day3\bank_balance.txt").readlines() as f:
# 	for i in f:
# 		print(i)
# print('1:',service_list[0])
# print('2:',service_list[1])
# print('3:',service_list[2])
# print('4:',service_list[3])
# print('5:',service_list[4])

# select_list = open(r"d:\python\study\data\day3\select_list.txt",'r',encoding='utf-8').readlines()
# for index,i in enumerate(select_list,1):							#生成序列打印列表
# 	print(index,i)
#
# print("\t菜单\n按0键退出系统\n按1返回上级系统\n按2返回主菜单")
import time
print(time.localtime())
print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()).split())
# print("还款成功\n请选择您需要的服务:\n 1、返回上级菜单\n2、退出系统")

# a = ['admin1','admin2','admin3','admin4']
#
# b = input("请输入账号")
# # for i in a:
# # 	if b not in a:
# if b not in a :
# 	a.append(b)
# print(a)
print("\t退出购物系统：quit\n\t查看购物城列表：car")


# a =['a','b','c']
# c =[]
# for i,j in enumerate(a):
# 	print(type(i))
# 	c.append(i)
#
# print(c)
#
# a= int(input("输入"))
# if a in c:
# 	print("success")
# print('1')
# print("你的购物清单如下：\n\n")
# print("物品"+'\t'+'数量'+'\t'+'价格'+'\t'+'加入时间'+'\n')
# a =[1,2,3,4,5]
# print(type(a[0]))
# print(sum(a))

# dict = {'a':1,"b":2,"c":3}
# for i in dict:
# 	print(i)
#
# for i,j in dict.items():
# 	print(i,j)
#
# a =map(lambda x :x+1,[2,3,4,5])
# print(type(a))
# for i in a :
# 	print(i)

# b = [1,2,3,4,5,6,7]
# a = set([1,2,3,4,5,6,7])
# c = set([2,3,4,5,1,6,0,9])
# print(c-a)
# # print(a+c)
# print(a)
# print(c)

d= 'bacnfnaiaifja  ahfaijfi '
print(d.find('a'))
print(d[-3:])
print(d[0])
print(d[1])
