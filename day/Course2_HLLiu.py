#  1   内置函数zip将list组合，再进行转换

keys = ['a','b','c']
values = [1,2,3]
print(dict(zip(keys,values)))




# 2 将字典按值（value）排序，dict ={1:2,3:4,4:3,2:1,0:0}         转换类型后进行sort


dict1 ={1:2,3:4,4:3,2:1,0:0}
list1 =dict1.items()										#转换
print(sorted(list1))										#key值排序

list2 = sorted([(x[1],x[0]) for x in list1] )				#交换位置生效序列在重新排毒
print([(x[1],x[0]) for x in list2 ])						#重新交换位置

print(sorted(list1,key=lambda a:a[1]))						#匿名函数结合sorted中的key条件

