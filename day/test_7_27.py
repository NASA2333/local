import time
import datetime
###练习函数调用、传参
# class Test():
# 	def sum(self):
# 		self.a = int(input("请给a赋值"))
# 		self.b = int(input("请给b赋值"))
# 		self.sum =self.a+self.b
# 		# print(self.sum)
# 		# return self.a,self.b
# 	def sub(self):
# 		self.sum()
# 		self.sub = self.a-self.b
# 		print(self.sub)
# if __name__=="__main__":
# 	a = Test()
# 	# a.sum()
# 	a.sub()
import unittest
from selenium.webdriver.support import expected_conditions as EC

'''
###用户输入数字，然后判断距离今天的天数


class Get_date():
	def get_year(self):
		try:
			self.year=int(input("请输入年份："))
		except Exception as msg:
			print("输入年份错误，请输入数字年份，范围（1900--当前年份")
			self.get_year()
		else:
			if self.year<1900 or self.year >2017:
				print("输入年份错误，请输入数字年份，范围（1900--当前年份")
				self.get_year()
		return self.year
	def get_month(self):
		try:
			self.month=int(input("请输入月份"))
		except Exception as msg:
			print("输入月份错误，请输入月份1--12：")
			self.get_month()
		else:
			if self.month>12 or self.month<1:
				print("输入月份错误，请输入月份1--12：")
				self.get_month()
			# else:
		return self.month
	def get_day(self):
		try:
			self.day =int(input("请输入日期："))
		except Exception as msg:
			print("请输入日期数字，1--31")
			self.get_day()
		else:
			if self.day >31 or self.day<1:
				print("日期输入错误，日期范围为1--31")
				self.get_day()
			elif self.month in (4,6,9,11):
				if self.day==31:
					print("日期输入错误，小月最大日期为30")
					self.get_day()
				else:
					return self.day
					# pass
			else:
				if (self.year%4==0 and self.year%100!=0) or self.year%400==0:		#闰年
					if self.month==2 and self.day>29:
						print("日期输入错误，闰年2月最大29")
						self.get_day()
				else:
					if self.month==2 and self.day>28:
						print("日期输入错误，平年2月最大为28日")
						self.get_day()
		return self.day
	def start(self):
		self.list =[]
		self.list.append(self.get_year())
		self.list.append(self.get_month())
		self.list.append(self.get_day())
		return self.list
	def date_sub(self):
		self.start()
		self.year_1 =self.list[0]
		self.month_1 =self.list[1]
		self.day_1 =self.list[2]

		now_time = time.strftime("%Y-%m-%d",time.localtime())
		now_time_list= now_time.split("-")
		self.year_2 =int(now_time_list[0])
		self.month_2 =int(now_time_list[1])
		self.day_2 =int(now_time_list[2])

		d1 = datetime.datetime(self.year_1,self.month_1,self.day_1)
		d2 = datetime.datetime(self.year_2,self.month_2,self.day_2)
		return  (d2-d1).days
if __name__ =="__main__":
	print(Get_date().date_sub())
'''
##九九乘法表

a = 1
b = 1
for i in range(1,10):
	for j in range(1,10):
		if j<i:
			print(j,"*",i,"=",i*j,end='\t')
		if j ==i:
			print(i,"*",j,"=",i*j,end='\n')

