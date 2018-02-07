'''
请使用python实现一个彩票机选程序：
1.其有五个菜单：a.新增，b.打印，c.删除,d.修改，e.退出
新增即为机选一注双色球，并追加到双色球列表，最多可以存十条记录，超过十条，提示用户是否要删除一条，是则执行删除菜单的功能

打印即输出当前双色球列表中的双色球列表（同时将双色球编号输出）
删除，可以根据用户输入的编号删除指定的双色球记录
修改，可以根据用户输入的编号修改双色球列表中指定的记录
退出，即退出当前程序，如双色球列表不为空，则提示用户是否继续退出
'''


import random,sys,time
pool = []						#选号池

def get_sum():
	'''
	生成号码
	'''
	list = []
	if len(pool)<10:
		list_6 = random.sample([x for x in range(1,34)],6)
		list_1 = random.sample([x for x in range(1,17)],1)
		list.append(list_6)
		list.append(list_1)
		pool.append(list)
		# out_pool()
		# list.clear()
		return  list
	else:
		print("对不起，您的选号池已经含有十组数据，想要继续操作在请输入1，取消请按2，退出请按0")
		while 1:
			try:
				choice = input("请输入您想要进行的操作：")
			except Exception as msg:
				print("您的输入有误，请重新输入")
				continue
			else:
				if int(choice)==1:
					del_pool()
					break
				elif int(choice) ==2:
					print("操作成功，请选择你想要的操作")
					break
				elif int(choice) ==0:
					print("系统将在三秒后退出，谢谢您的使用")
					time.sleep(3)
					sys.exit()
				else:
					print("您输入的选项不存在，请重新选择")

def del_pool():
	out_pool()
	while 1:
		try:
			choice_del =input("请输入你想要删除数据的序号")
		except Exception as msg:
			print("对不起，您的输入有误，请重新输入")
			continue
		else:
			index_list_del=[]
			for index,value in enumerate(pool):
				index_list_del.append(index+1)
			# print(index_list_del)
			# print(type(index_list_del[1]))
			if int(choice_del) in index_list_del:
				del pool[int(choice_del)-1]
				index_list_del.clear()
				break
			else:
				print("您输入的序号不存")

def out_pool():
	# print(pool)
	if len(pool)==0:
		print(pool)
	else:
		for index,num in enumerate(pool):
			print(index+1,':\t\t',num)

def exit_pool():
	print("系统将在三秒后退出，感谢您的使用，再见")
	time.sleep(3)
	sys.exit()

def updata_pool():
	while 1:
		out_pool()
		try:
			choice_update= input("请输入您想要修改数据的序号")
		except Exception as msg:
			print("对不起，您的输入有误，请重新输入")
			continue
		else:
			index_list=[]
			for index,value in enumerate(pool):
				index_list.append(index+1)
			if int(choice_update) in index_list:
				# pool[int(choice_update)-1] =get_sum()
				del pool[int(choice_update)-1]				#删除
				# print(pool)
				# get_sum()
				# pool[int(choice_update)-1],pool[]
				pool.insert((int(choice_update)-1),get_sum())
				del pool[-1]
				index_list.clear()
				break
			else:
				print("您输入的序号不存")

def start():
	while 1:
		print("\t\t欢迎使用双球球选号系统\n请选择你想要执行的操作：\na\t新增\nb\t打印\nc\t删除\nd\t修改\ne\t退出")
		try:
			choice_start =input("请输入你想要的操作：")
			# print(choice_start)
			# print(type(choice_start))
		except Exception as msg:
			print("您的输入有误，请重新选择")
			continue
		else:
			if choice_start =='a':
				get_sum()
			elif choice_start =='b':
				out_pool()
			elif choice_start =='c':
				del_pool()
			elif choice_start =='d':
				updata_pool()
			elif choice_start =='e':
				print("感谢您的使用，系统将在三秒后退出，再见")
				sys.exit()
			else:
				print("对不起，你输入的选项不存在")



start()