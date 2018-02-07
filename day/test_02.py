#用户输入日期，判断距离今天多少天
import datetime
import time
class Get_date():

	def get_year(self):
		self.list =[]
		try:
			self.year = int(input("请输入年份"))
		except ValueError as msg:
			print("年份输入错误")
			self.get_year()
		else:
			if self.year<1900 or  self.year>2017:
				self.get_year()
			else:
				self.get_month()
				self.list.append(self.year)
			return self.list
	def get_month(self):
		try:
			self.month = int(input("请输入月份"))
		except ValueError as msg:
			print("月份输入错误")
			self.get_month()
		else:
			if self.month<1 or self.month>12:
				self.get_month()
			else:
				self.get_day()
				self.list.append(self.month)
			# return self.list
	def get_day(self):
		try:
			self.day = int(input("请输入日期"))
		except ValueError as msg:
			print("日期输入错误")
			self.get_day()
		else:
			if self.day<1 or self.day>31:
				print("日期输入错误")
				self.get_day()
			elif self.month in(4,6,9,11):
				if self.day==31:
					print("该月没有31天")
					self.get_day()
				else:
					self.list.append(self.day)
				# return self.list
			else:
				if self.month ==2:
					if (self.year%4==0 and self.year%100 !=0) or self.year%400==0:
						if self.day>29:
							print("该月份最多为29天")
							self.get_day()
						else:
							self.list.append(self.day)
						# return self.list
					else:
						if self.day>28:
							print("该月最大为28")
							self.get_day()
						else:
							self.list.append(self.day)
						# return self.list
				else:
					self.list.append(self.day)
			return self.list

class Date():
	get_date =Get_date()
	list =get_date.get_year()
	def sum(self):
		self.run =int[31,60,91,121,152,182,213,244,274,305,335,366]
		self.ping =int[31,59,90,120,151,181,212,243,273,304,334,365]
		self.sum = 0
		self.year =list[2]
		self.month = list[1]
		self.day = list[0]
		self.sum_year = 2017-self.year
		for i in range(self.sum_year):
			self.now_year = self.year+i
			if (self.now_year%4==0 and self.now_year%100 !=0) or self.now_year%400==0:
				self.sum = self.sum+366
				return  self.sum
			else:
				self.sum = self.sum+365
				return self.sum
		if (self.year%4==0 and self.year%100 !=0) or self.year%400==0:
			self.sum = self.sum -self.run[self.month-2]-self.day-1
			return self.sum
		else:
			self.sum = self.sum -self.ping[self.month-2]-self.day-1
class Get_sum():
	def get_sum(self):
		self.year_1 =Get_date().get_year()[2]
		self.month_1 =Get_date().get_year()[1]
		self.day_1=Get_date().get_year()[0]
		return  self.year_1,self.month_1,self.day_1
if __name__ =="__main__":
	# a = Get_date().get_year()
	# print(a)
	time1 = time.strftime("%Y-%m-%d",time.localtime())
	print(time1)
	# year_1 =Get_date().get_year()[2]
	# month_1 =Get_date().get_year()[1]
	# day_1=Get_date().get_year()[0]
	# #
	a = Get_sum().get_sum
	years = time1.split("-")
	year_2 = years[0]
	month_2 = years[1]
	day_2 = years[2]

	d1 = datetime.datetime(int(a.year_1),int(a.month_1),int(a.day_1))
	d2 = datetime.datetime(int(year_2),int(month_2),int(day_2))

	print((d2-d1).days)
