#1、假设要用50、20、10、5、1（元）来找零，给定任意小于100且为整数的找零金额，求最少找零张数

''' 依次求商、求模，上一次的模是下一次的被除数'''
"""
while 1:
	try:
		money = int(input("请输入找零金额（ps：正整数）:"))
		break
	except Exception as msg:
		print("输入有误，请重新输入")

option = [50,20,10,5,1]							#找零面额
sumlist=[]
for i in option:
	choice = divmod(money,i)
	if choice[1] ==0:
		sumlist.append(choice[0])
		break
	else:
		sumlist.append(choice[0])
		money = choice[1]
print("最少找零张数：",sum(sumlist))

"""


#2、给出一串字符串，求出该字符串中最长的回文字符串
		# 例如：
       	# 		给定字符串为 "babad"
	   	# 		Output: "bab" or "aba"

''' 先求出字符串中所有回文字符串，再根据长度取值  '''
"""
inputstr = input("请输入需要判断的字符：")
L =[]
for i in range(len(inputstr)+1):
	for j in range(i+1,len(inputstr)+1):
		if inputstr[i:j] ==inputstr[i:j][::-1]:
			L.append(inputstr[i:j])
print(L)
print(max(L,key=len))
"""

#3、给定一个由字符串组成的列表，将由相同字符组成的字符串归并在一起
		# list = ['ilsi', 'lsii', 'sili',  'isli,  'ilis',  'siil','rmp', 'prm', 'pmr', 'mrp', 'mpr', 'rpm','kema',  'make',
		# 'meak', 'mkae',  'ekma', 'meka',  'amke', 'kmae', 'test']
		#
		# Output:[['isli','lsii'.......],['mpr','pmr'....],['make','ekma'....],['test']]

'''每个单词进行排序，再归类'''
# liststr = ['ilsi','lsii','sili','isli','ilis','siil','rmp','prm','pmr','mrp','mpr','rpm','kema', 'make',
# 	'meak','mkae','ekma','meka','amke','kmae','test']
#
# dicts = {}
# for s in liststr:
# 	strs1 = ''.join(sorted(s))
# 	if strs1 not in dicts:
# 		dicts[strs1] =[s]
# 	else:
# 		dicts[strs1].append(s)
#
# print(list(dicts.values()))
