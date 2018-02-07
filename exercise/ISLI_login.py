from python import base   #公用模块
from selenium import  webdriver
import time,unittest
import HTMLTestRunner
# url = r"http://www.baidu.com"
# a = base.BasePage()
# a.open(url,t="百度一，你就知道")
# a.send_keys(("i","kw"),"selenium")
# a.close()

class Beta(unittest.TestCase):
	def setUp(self):
		self.driver = base.BasePage()
		self.url = r"https://172.16.5.161:8443/mpr/portal-mcrs-publisher/mvc/publisher/toLogin"
		self.driver.open(self.url)
	def test_login_error_name(self):
		u""" 账号不存在		"""
		self.driver.send_keys(("css","#userName"),"mpr_2013")
		self.driver.send_keys(("id","passWord"),"123456")
		self.driver.send_keys(("class name","code"),"8888")
		self.driver.click(("class name","btn"))
		time.sleep(2)
		self.error_tip =self.driver.find_element(("id","error_tips")).text
		self.assertEqual("账户不存在！",self.error_tip)

	def test_login_error_pw(self):
		u""" 密码错误		"""
		self.driver.send_keys(("css","#userName"),"mpr_20130008")
		self.driver.send_keys(("id","passWord"),"123456")
		self.driver.send_keys(("class name","code"),"8888")
		self.driver.click(("class name","btn"))
		res =self.driver.is_text_in_element(("id","error_tips"),"密码错误")
		self.assertTrue(res)

	def test_login_error_pw_less(self):
		u""" 密码小于6位		"""
		self.driver.send_keys(("css","#userName"),"mpr_20130008")
		self.driver.send_keys(("id","passWord"),"1236")
		self.driver.send_keys(("class name","code"),"8888")
		self.driver.click(("class name","btn"))
		error_tip =self.driver.find_element(("id","errorPassWord")).text
		self.assertEqual("密码最小为6位",error_tip)

	def test_login_name_none(self):
		u""" 用户名为空		"""
		self.driver.send_keys(("css","#userName"),"")
		self.driver.send_keys(("id","passWord"),"123456")
		self.driver.send_keys(("class name","code"),"8888")
		self.driver.click(("class name","btn"))
		res =self.driver.is_text_in_element(("id","errorUserName"),"您还没有输入用户名")
		self.assertTrue(res)

	def test_login_error_pw_none(self):
		u""" 密码为空		"""
		self.driver.send_keys(("css","#userName"),"mpr_20130008")
		self.driver.send_keys(("id","passWord"),"")
		self.driver.send_keys(("class name","code"),"8888")
		self.driver.click(("class name","btn"))
		error_tip =self.driver.find_element(("id","errorPassWord")).text
		self.assertIn("您还没有输入密码",error_tip)

	def test_login_error_code_none(self):
		u""" 验证码为空		"""
		self.driver.send_keys(("css","#userName"),"mpr_20130008")
		self.driver.send_keys(("id","passWord"),"123611")
		self.driver.send_keys(("class name","code"),"")
		self.driver.click(("class name","btn"))
		error_tip =self.driver.find_element(("id","errorCodeCon")).text
		self.assertEqual("您还没有输入验证码",error_tip)

	def test_login_success(self):
		u""" 登入成功"""
		self.driver.send_keys(("css","#userName"),"mpr_20130008")
		self.driver.send_keys(("id","passWord"),"aaaaaa")
		self.driver.send_keys(("class name","code"),"8888")
		self.driver.click(("class name","btn"))
		time.sleep(3)
		name =self.driver.find_element(("css",".paddings>a")).text
		self.assertIn("天朗闻听（北京）图书",name)

	def tearDown(self):
		self.driver.close()

if __name__=="__main__":
	unittest.main()