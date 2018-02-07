from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
class Action(object):
	"""
	封装公共方法
	"""
	#初始化
	def __init__(self,selenium_driver,base_url,pagetitle):
		self.base_url =base_url
		self.pagetitle = pagetitle
		self.driver = selenium_driver

	#获取页面title     reutn 1 or 0
	def on_page(self,pagetitle):
		return pagetitle in self.driver.title

	#校验页面正常加载
	def open(self,url,pagetitle):
		self.driver.get(url)
		self.driver.maximize_window()
		assert self.on_page(pagetitle),"打开页面失败 %s" %url

	#定位元素
	# def find_element(self,):





