import unittest
from ddt import ddt,data
import xlrd
import  time
from selenium import webdriver
xlsdata = []
class finddata():
	xls  =xlrd.open_workbook(r'D:\python\test\data\baidu_search.xls').sheet_by_index(0)
	nrows = xls.nrows

	for i in range(1,nrows):
		r ={}
		a =xls.row_values(i)
		# print(a)
		r['key'] =a[0]
		r['ass'] =a[1]
		# print(r)
		xlsdata.append(r)

	# print(xlsdata)

@ddt
class Testsearch(unittest.TestCase):
	def setUp(self):
		self.ob = webdriver.Firefox()
		self.ob.get(r"http://www.baidu.com")

	def search(self,key,title):
		self.ob.find_element_by_id('kw').send_keys(key)
		self.ob.find_element_by_id('su').click()
		time.sleep(2)
		title_key = self.ob.title
		self.assertEqual(title_key,title)
	@data(*xlsdata)
	def test_01(self,data):
		self.search(data['key'],data['ass'])


	def tearDown(self):
		self.ob.close()



