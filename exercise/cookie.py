# from selenium import  webdriver
# import time
#
# driver = webdriver.Firefox()
# driver.get("")


import requests,time,json
import re

"""
"__csrf__=B%40iem754447fd70a72f9e579ca&__form__=1&__dialog__=1&username=liuhl%40mpreader.com&password=liuhonglian19930"
data = {"__csrf__":"B%40jirdlleze026e928e1215e5b","__form__":'1',"__dialog__":1,'username':'liuhl%40mpreader.com','password':'liuhonglian19930'}
# __csrf__=B%40qu4453ctb1d3dee15a6f707b&__form__=1&__dialog__=1&username=liuhl%40mpreader.com&password=liuhonglian19930
header = {"Cookie":"phsid=A%2F4hwcfpocjpth54rg36rxgkxe77df5arjjhbjkzsv; next_uri=1500357010%2C%2F; phcid=rieqksfodkp56kme",
		  "Content-Type":"application/x-www-form-urlencoded"
		  }

# header = {
# 	"Host": "review.mprtimes.net",
# "Connection": "keep-alive",
# "Cache-Control": "max-age=0",
# "Origin":"null",
# "Upgrade-Insecure-Requests": "1",
# "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
# "Content-Type": "application/x-www-form-urlencoded",
# "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
# "Accept-Encoding": "gzip, deflate",
# "Accept-Language": "zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4,ja;q=0.2",
# "Cookie":"phsid=A%2F4hwcfpocjpth54rg36rxgkxe77df5arjjhbjkzsv; next_uri=1500357010%2C%2F; phcid=rieqksfodkp56kme"

# }
r = requests.session()
r1 = r.post(url="http://review.mprtimes.net/auth/login/password:self/",headers = header,data=data,verify=False)

"""

'''
# r = requests.session()
# r1 = r.get(url="http://review.mprtimes.net/")
# # print(dict(r1.cookies))
# data_cookie = dict(r1.cookies)
# header = {"Content-Type":"application/x-www-form-urlencoded"}
# # header.update(Cookie=data_cookie)
# header['Cookie'] =data_cookie
# print(str(header))
#
# data = {"__csrf__":"B%40jirdlleze026e928e1215e5b","__form__":'1',"__dialog__":1,'username':'liuhl%40mpreader.com','password':'liuhonglian19930'}
# r2 = r.post(url='http://review.mprtimes.net/auth/login/password:self/',data=data,headers =json.loads(str(header)))
# print(r2.text)
'''
class Login_ph(object):

	def __init__(self):
		self.url_open ="http://review.mprtimes.net/"
		self.url_login="http://review.mprtimes.net/auth/login/password:self/"
		self.url_search=r"http://review.mprtimes.net/maniphest/query/advanced/"
		self.s = requests.session()
		self.headers={
			"Accept":"text/html,application/xhtml+xml,application/xml",
			"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
			"Cookie":"phsid=A%2Flbr3jzoqrkrc6uzie3nep2jq4t7z5wzcsvdvfwvc; phcid=4s25wigwxpe32s6l; next_uri=1500446150%2C%2F; _ga=GA1.2.685703157.1496907371; _gid=GA1.2.757828365.1500251483; hibext_instdsigdip=1"


		}
		self.s.verify=False
###获取csrf
	def get_csrf_token(self):
		login_page = self.s.get(self.url_open)
		text = re.findall(r'"current":"(.+?)"',login_page.text)
		self.csrf =text[0]
		# scrf = login_page.cookies['__csrf__']
		# print(scrf)
		print(self.csrf)
		return self.csrf

	def post_login(self):
		self.csrf = self.get_csrf_token()
		from_data = {
			"__csrf__": self.csrf,
			"__form__":1,
			"__dialog__":'1',
			"username":"HLLiu",
			"password":"liuhonglian19930"

		}
		r = self.s.post(self.url_login,data=from_data)
		# print(r.text)
		text = re.findall(r'"current":"(.+?)"',r.text)
		self.csrf =text[0]
		print(r.status_code)
		print(r.history)
		print(self.csrf)
		# return self.csrf
	def search(self):
		# self.csrf  = self.get_csrf_token()
		Login_ph.post_login(self)
		search_data ={"__csrf__":self.csrf,
					"__form__":1,
					"fulltext":"中国isli",
					"blocking":"",
					"blocked":"",
					"group":"priority",
					"order":"priority",
					"createdStart":"",
					"createdEnd":"",
					"modifiedStart":"",
					"modifiedEnd":"",
					"limit":""

		}
		r = self.s.post(self.url_search,data=search_data)

		print(r.status_code)
		print(r.history)
		print(r.url)
		print(r.text)


if __name__=="__main__":
	Login_ph().search()


from selenium import  webdriver
ob= webdriver.Firefox()
ob.find_element_by_class_name()



