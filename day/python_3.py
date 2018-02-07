'''
利用while、for、if等制作出一个增删查员工的姓名和信息的小程序
个人信息包括：姓名(name)、工号(number)、职位(job)、爱好(hobby)
test_info = {'caolh':{'number':'0001','job':'test','hobby':'play basketball'}}
要求如下：
一、能够查找、增加、删除员工的姓名和个人信息以及退出等常用操作，如下，输入1表示查询，输入2表示新增
		1：查询员工信息，用for遍历字典打印员工信息，如下:
			caolh的工号是0001
				职位是test
				爱好是play basketball
		2：增加新员工的个人信息，如果员工已存在提示是否覆盖并重新创建
		3：删除已有的员工
		4：退出程序
二、对于输入错误进行处理，满足输入条件在进行下一步
'''
"""
还有几种情况没做优化处理eg：打印为空等

"""


import  sys,time

class Staff():
	def __init__(self):
		self.data = {}

	def add_data(self):
		self.name = input("请输入姓名：")
		if self.name in self.data:
			return self.choice()
		else:
			return self.input_data()

	def input_data(self):
		mean = {}
		number = input("请输入您的工号：")
		job= input("请输入您的工作：")
		hobby = input("请输入您的爱好：")
		mean['number'] = number
		mean['job'] = job
		mean['hobby'] = hobby
		self.data[self.name] =mean
		print("恭喜您，账号添加成功")
		return self.menu()

	def get_data(self):
		for i in self.data:
			print("\t %s的工号是： %s\n\t\t 职位是：%s \n\t\t 爱好是： %s \n"%(i,self.data[i]['number'],self.data[i]['job'],self.data[i]['hobby']))
		# return self.menu()
		self.menu()

	def choice(self):
		print("对不起，你的账户已存在，请选择接下来的操作")
		while 1:
			try:
				choice =int(input("输入‘0’覆盖之前用户\n输入‘1’放弃当前操作"))
			except Exception as msg:
				print("对不起，您的输入有误，请重新选择")
			else:
				if choice ==0:
					return  self.input_data()
				elif choice ==1:
					return  self.menu()
				else:
					print("您输入的选项不存在，请重新输入")

	def del_data(self):
		while 1:
			name = input("请输入你想要删除的账号：")
			if name not in self.data:
				print("你输入账号不存在")
				while 1:
					choice =input("继续选择账号删除请按1，放弃删除操作请按0")
					if choice =='1':
						break
					elif choice =='0':
						return self.menu()
					else:
						print("对不起，您输入的选项不存在，请重新选择")
			else:
				del self.data[name]
				print("账号删除成功，系统将回到主页面")
				return self.menu()

	def menu(self):
		print("欢迎来到员工信息系统")
		while 1:
			try:
				choice =int(input("请选择你想要进行的操作\n1:\t查询\n2:\t新增\n3:\t删除\n4:\t退出系统"))
			except Exception as msg:
				print("对不起，你的输入有误，请重新选择")
			else:
				if choice ==1:
					return self.get_data()
				elif choice ==2:
					return self.add_data()
				elif choice ==3:
					return self.del_data()
				elif choice ==4:
					print("感谢您的使用，系统将在3s后退出，感谢您的使用")
					time.sleep(3)
					sys.exit()
				else:
					print("您输入的选项不存在，请重新进行选择")


if __name__ =="__main__":
	a = Staff()
	a.menu()