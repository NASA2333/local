'''
抓取免费ssh账号
'''

from selenium import  webdriver
import  time

class Getdata():

	def get_data(self):
		'''
		获取数据
		:return:
		'''

		ob = webdriver.Firefox()
		ob.get(r"https://free-ss.site/")
		time.sleep(2)
		a1 = ob.find_elements_by_css_selector("[role ='row']>td:nth-child(2)")
		a2 = ob.find_elements_by_css_selector("[role ='row']>td:nth-child(3)")
		a3 = ob.find_elements_by_css_selector("[role ='row']>td:nth-child(4)")
		a4 = ob.find_elements_by_css_selector("[role ='row']>td:nth-child(5)")
		a5 = ob.find_elements_by_css_selector("[role ='row']>td:nth-child(6)")

		iplist = [i.text for i in a1]
		portlist = [i.text for i in a2]
		pwlist =[i.text for i in a3]
		methodlist = [i.text for i in a4]
		verified =[i.text for i in a5]
		self.list1 = zip(iplist,portlist,pwlist,methodlist)
		time.sleep(2)
		ob.close()

	def writ_data(self):
		'''
		写入数据,去重
		:return:
		'''
		self.get_data()
		read_book = open(r'E:/ssh.txt','r')							#读取本地
		z=read_book.read()
		finallist = []

		for i in self.list1:										#网上
			# print(type(i))
			if str(i) not in z:
				if '107.170.196.108' not in str(i):
					finallist.append(i)
			else:
				pass
		read_book.close()
		print(finallist)

		book = open(r"E:/ssh.txt",'a')
		for i in finallist:
			book.write(str(i)+'\n')
		book.close()

if __name__ =="__main__":
	# while 1:
	# 	time.sleep(900)
	# 	a = Getdata()
	# # 	# a.get_data()
	# 	a.writ_data()
	a = ()
	print(type(a))
	print(a)
	if a :
		print(1)
	else:
		print(2)