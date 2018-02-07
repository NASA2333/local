dict1 = {'a':'test1','b':{'c':'test2','d':'test3','e':'test4'},'f':'test5','g':'test6','h':{'i':'test7','j':'test8'}}

#输入key值导出value
num = input("请输入key值：")
#
# for i in dict:
# 	if num ==i:
# 		print(dict[i])
# 	else:
#
new_dict ={}
list = []
def newdict(dicts):
	for i in dicts:
		new_dict[i] =dicts[i]
		# print(new_dict)
		if isinstance(dicts[i],dict):
			get_value(dicts[i])
get_value(dict1)
for j in new_dict:
	list.append(j)
if num in list:
	print(num,':',new_dict[num])
else:
	print("对不起，你输入的key值不存在")