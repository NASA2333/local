'''
思路：  1、单个api请求能成功
				request进行请求
		2、用unittest
				获取key，syestemd的请求独立成一个函数，方便调用
				每个接口写成一个单独的类
		3、htmlrunner生成测试报告
'''
#
# #time
# #
# import unittest,requests,hashlib,time,json
# class Api_all(unittest.TestCase):
# 	def setUp(self):
# 		self.time =str(int(time.time()*1000))
# 		m2 =hashlib.md5()
# 		scr = '722d50a9-28d4-4cba-b226-ca1f1115f37d'+ self.time
# 		m2.update(scr.encode('utf-8'))
# 		self.ticket = m2.hexdigest()
# 		# header = {'publisherId':'1386833104009','timestamp':time1,'ticket':ticket,'systemId':'469b235f-3ef1-4472-9892-055af1ede259'}
# 		self.header = {'publisherId':'1386833104009','timestamp':self.time,'ticket':self.ticket,'systemId':'469b235f-3ef1-4472-9892-055af1ede259'}
# 	def test_001(self):
# 		r= requests.get(url='http://172.16.5.162:8080/mpr/portal-mcrs-openapi/mvc/mprcode/getVendorInfo',headers=self.header,params={'typeId':'0','clientType':'mpr'})
# 		# print(r.json())
# 		a= (r.content).decode('utf-8')
# 		print(json.loads(a).get('respCode'))
# 		# print((r.content).decode('utf-8'))
# 		# print(json.loads(r.content))
# 		# # print(eval(r.text).get('respCode'))
# 		# a = json.loads(r.text)
# 		# print(type(a))
# 		# # a = exec('c='+r.content)
# 		# # print(a.get('respCode'))
#
#
# 		# print(self.resp)
#
# 	def tearDown(self):
# 		pass



#
# from selenium import webdriver
#
# import time
#
# ob = webdriver.Firefox()
# ob.get("http://172.16.3.112:8080/versionserver/static/index.html#/publish/login")
# time.sleep(6)
#
# ob.find_element_by_tag_name("button").click()


import random

# a = [random.sample(1,34) for i in range(6)]
# print(a)
# a =[i for i in range(1,34)]
# b = random.sample([i for i in range(1,34)],6)
# print(type(b))
# d = random.randint(1,16)
# print(d)
# e = b.append(d)
# print(e)
# c =random.sample([i for i in range(1,34)],6).append(random.randint(1,16))
# print(c)

a = random.uniform(1,2)
print(a)








#
