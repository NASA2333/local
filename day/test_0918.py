import xlrd,sys
class Login():
	def __init__(self):
		self.user_file = r'D:\python\study\data\day3\user.xls'						#账户
		self.user_lock=r"D:\python\study\data\day3\user_lock.txt"					#锁定账户
		self.bank_balance =r'D:\python\study\data\day3\bank_balance.txt'			#余额
		self.deal_list_file=r'D:\python\study\data\day3\deal_list.txt' 				#交易记录

	def read_xls(self,file,row=0,y=0):
		self.xls =xlrd.open_workbook(file).sheet_by_index(0)
		self.xls_nrows = self.xls.nrows			#行数
		self.xls_ncols = self.xls.ncols
		self.xls_cow_value = self.xls.col_values(row)  #获取列值
		self.xls_cell =self.xls.cell_value(y,1)		#获取单元格数据


	def account_disabled(self,user):
		#判断用户是否被禁用
		fp = open(self.user_lock).readlines()
		# print(fp)
		# self.existence_account()
		for i in fp:
			line = i.split()[0]
			if user == line:
				print("您的账号已被锁定")
				sys.exit()

	def existence_account(self,user):
		#判断账号存在
		self.read_xls(self.user_file)
		for index,i in enumerate(self.xls_cow_value):
			if user ==i:
				return index		#用户名序列号
			else:
				pass

	def existence_accountpw(self):
		#判断密码是否正确
		index_1 = self.existence_account(self.user)
		self.read_xls(self.user_file,y=int(index_1))

		while self.count<self.coun_limit:
			self.pw = input("请输入密码：")
			if self.pw  ==self.xls_cell:
				# print("恭喜你登入成功")
				return True
			else:
				self.count +=1
				print("密码输入错误，请重试")
		else:
			print("你将被锁定")
			file = open(a.user_lock,'a')
			file.write(self.user+'\n')
			file.close()

	def bank_login(self):
		#登入
		self.count = 0
		self.coun_limit = 3
		while self.count<self.coun_limit:
			self.user = input("请输入账号")
			self.account_disabled(self.user)
			if not self.existence_account(self.user):
				print("您输入的账号不存在")
				continue
			elif self.existence_accountpw():
				return "账号登入成功"

if __name__ =="__main__":
	a = Login()
	c =a.bank_login()
	print(c)
	print(bool(c))
	if c=="账号登入成功":
		print('条件判断后继续执行')