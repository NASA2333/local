import time,requests,os,sys
from  bs4 import BeautifulSoup

if hasattr(sys, "frozen"):
	application_path = os.path.dirname(sys.executable)
	xpath =application_path
else:
	xpath = os.path.dirname(__file__)

class GetInfo():
	def __init__(self):
		self.dates = time.strftime("%Y-%m-%d %H-%M-%S",time.localtime())
		self.parms = {'user_time':str(self.dates),'version':'2017-09-04 14:36',"protocol":'https'}
		# self.xpath = os.path.dirname(__file__)
		if not os.path.exists(os.path.join(xpath,'cross_talk')):
			os.makedirs(os.path.join(xpath,'cross_talk'))
		user_agent ="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36"
		self.headers = {'User-Agent': user_agent,
                        "Accept-Encoding": "gzip, deflate, br",
                        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7,ja;q=0.6",
                        "Cache-Control": "no-cache"}

	def get_hot(self):
		url_1 =r'https://www.qiushibaike.com/8hr/page/'
		num =1
		while num <=13:
			url = url_1+str(num)
			# print(url)
			r= requests.get(url,params=self.parms,headers =self.headers)
			a = r.text
			soup = BeautifulSoup(a,'html.parser')

			b = soup.find_all(class_='content')
			# print(b)
			file  = open(os.path.join(xpath,r'cross_talk\hot.txt'),'a',encoding='utf-8')			#写入编码
			z =1
			for i in b:
				x = i.text
				file.write(str(z)+":"+x.strip()+"\n")
				z+=1
			file.close()
			num+=1
			time.sleep(2)

	def get_hot24(self):
		url_1 =r'https://www.qiushibaike.com/hot/page/'
		num =1
		while num<=13:
			url =url_1+str(num)
			# self.parms['url']="https://www.qiushibaike.com/hot/page/"+str(num)
			r = requests.get(url,params=self.parms,headers =self.headers)
			soup = BeautifulSoup(r.text,'html.parser')
			alltext = soup.find_all(class_='content')

			file = open(os.path.join(xpath,r'cross_talk\hot24.txt'),'a',encoding='utf-8')
			for i in alltext:
				file.write(str(alltext.index(i))+":"+i.text.strip()+"\n")
			file.close()
			num +=1
			time.sleep(2)

	def get_history(self):
		url_1 =r'https://www.qiushibaike.com/history/'
		num =1
		while num<=20:
			url =url_1+str(num)
			r = requests.get(url,params=self.parms,headers =self.headers)
			soup = BeautifulSoup(r.text,'html.parser')
			alltext = soup.find_all(class_='content')

			file = open(os.path.join(xpath,r'cross_talk\historytxt.txt'),'a',encoding='utf-8')
			for i in alltext:
				file.write(str(alltext.index(i))+":"+i.text.strip()+"\n")
			file.close()
			num +=1
			time.sleep(2)

	def get_new(self):
		url_1 = r'https://www.qiushibaike.com/textnew/page/'
		num =1
		while num<=35:
			url =url_1+str(num)
			r = requests.get(url,params=self.parms,headers =self.headers)
			soup = BeautifulSoup(r.text,'html.parser')
			alltext = soup.find_all(class_='content')

			file = open(os.path.join(xpath,r'cross_talk\new.txt'),'a',encoding='utf-8')
			for i in alltext:
				file.write(str(alltext.index(i))+":"+i.text.strip()+"\n")
			file.close()
			num +=1
			time.sleep(2)

	def get_char(self):
		url_1 =r'https://www.qiushibaike.com/text/page'
		num =1
		while num<=20:
			url =url_1+str(num)
			r = requests.get(url,params=self.parms,headers =self.headers)
			soup = BeautifulSoup(r.text,'html.parser')
			alltext = soup.find_all(class_='content')

			file = open(os.path.join(xpath,r'cross_talk\chartxt.txt'),'a',encoding='utf-8')
			for i in alltext:
				file.write(str(alltext.index(i))+":"+i.text.strip()+"\n")
			file.close()
			num +=1
			time.sleep(2)


if __name__ =="__main__":
	a = GetInfo()
	print("抓取即将开始，请稍等.....")
	try:
		a.get_hot24()
		print("‘24小时热门’栏目抓取完毕")
		a.get_hot()
		print("‘热门’栏目抓取完毕")
		a.get_char()
		print("‘文字’栏目抓取完毕")
		a.get_new()
		print("‘新鲜’栏目抓取完毕")
		a.get_history()
		print("‘穿越’栏目抓取完毕")
	except Exception as msg:
		print("抓取失败","\n"*2)
		print(msg)
		time.sleep(50000)
	else:
		print("抓取成功，请进入文件中查看，系统将在20秒后退出")
		i = 0
		if i <=20:
			time.sleep(1)
			if i%5 ==0:
				print("系统将在%s 秒后退出"%(20-1))
			i+=1


