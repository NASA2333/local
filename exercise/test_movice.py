'''

按照下面的要求实现对列表的操作：
      1）产生一个列表，其中有40个元素，每个元素是0到100的一个随机整数
      2）如果这个列表中的数据代表着某个班级40人的分数，请计算成绩低于平均分的学生人数，并输出
      3）对上面的列表元素从大到小排序
'''

# import random
# list = []
# for i in range(40):
# 	a = random.randint(0,100)
# 	list.append(a)
# c= sum(list)/40
# print(c)
# print(sorted(list,reverse=True))
# print(len(list))

"""
有一个列表，其中包括10个元素，例如这个列表是[1,2,3,4,5,6,7,8,9,0],
要求将列表中的每个元素一次向前移动一个位置，第一个元素到列表的最后，然后输出这个列表。最终样式是[2,3,4,5,6,7,8,9,0,1]
"""
# import random
# list = []
# for i in range(10):
# 	a = random.randint(0,100)
# 	list.append(a)
# print(list)
# for i in range(len(list)-1):
# 	list[i],list[i+1]=list[i+1],list[i]
# 	print(list)

list = [[1,2,3,4,5,6],
		[2,3,4,5,6,7],
		[3,4,5,6,7,8],
		[4,5,6,7,8,9,]
		]
print(list[1][1])
print(list[1:2][0])
print(map(list[1],list[2]))
print(dict(zip(list[1],list[2])))
# for i in  range(len(list)):
# 	print(list[i][5])