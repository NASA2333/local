#coding=utf-8
import requests,urllib.request,re,os,time
from bs4 import BeautifulSoup
from tomorrow import threads
import socket


class Get_image():
	def __init__(self):
		self.datas = input("请输入你想要下载图片的关键字：")
		self.num =int(input("请输入您想下载图片张数（输入20的整数倍，最大为2000）："))

	def get_image(self):
		user_agent ="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36"
		headers = {'User-Agent': user_agent, "Upgrade-Insecure-Requests": '1',
                        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
                        "Accept-Encoding": "gzip, deflate, sdch",
                        "Accept-Language": "zh-CN,zh;q=0.8,en;q=0.6",
                        "Cache-Control": "no-cache"}

		# prmas ={"tn":"resultjson_com","ipn":"rj","ct":201326592,"fp":"result","queryWord":self.datas,"cl":2,"lm":-1,"ie":"utf-8","oe":"utf-8",
		# 	"st":-1,"ic":0,"word":self.datas,"face":0,"istype":2,"nc":1,"pn":30,"rn":30,"gsm":"7bc"}
		# url = r"https://image.baidu.com/search/acjson"
		# #urls = r"http://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord="+self.datas+"&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&word="+ self.datas +"&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&pn=30&rn=30&gsm=1000000001e&1486375820481="
		# url_init_first = r'http://image.baidu.com/search/flip?tn=baiduimage&ipn=r&ct=201326592&cl=2&' \
		# 				 r'lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1497491098685_R&pv=&ic=0&nc=1&z=&se=1&' \
		# 				 r'showtab=0&fb=0&width=&height=&face=0&istype=1&ie=utf-8&ctd=1497491098685%5E00_1519X735&word='
		# url_init = url_init_first + urllib.parse.quote(self.datas, safe='/')
		# print(url_init)

		prmas ={"tn":"baiduimage","ie":"utf-8","pn":0,"gsm":"50","ic":0,"lm":-1,"width":0,"height":0,"word":self.datas}
		urls =r'http://image.baidu.com/search/flip'
		respon = requests.get(url=urls,params =prmas,headers =headers)
		self.imageurl_list =[]
		n = 1
		while prmas['pn'] <self.num:
			respon = requests.get(url=urls,params =prmas,headers =headers)
			# print(respon.text)
			# print(respon.url)
			try:
				# imageurl =re.findall(r'(?<=objurl":").*?(?=",)',respon.text)
				imageurl= re.findall(r'"objURL":"(.*?)",',respon.text)
				# imageurl = re.findall('"objURL":"(.*?)",', respon.text, re.S)
				if n%3==1:
					self.imageurl_list.extend(imageurl[0:21])
				elif n%3 ==2:
					self.imageurl_list.extend(imageurl[21:41])
				else:
					self.imageurl_list.extend(imageurl[41:60])
				# prmas['pn'] +=30
			except Exception as msg:
				pass
			finally:
				n+=1
				prmas['pn'] +=20
		return self.imageurl_list

	@threads(10)
	def save_image(self):
		self.get_image()
		x = 0
		n = 1
		for i in set(self.imageurl_list):
			# print("正在保存第 %s 张图片......"%x)
			paths = os.path.join(r'D:\baidu_image',self.datas)
			if not os.path.exists(paths):
				os.makedirs(paths)
			try:
				socket.setdefaulttimeout(15)
				urllib.request.urlretrieve(i,os.path.join(paths,"%s.jpg"%x))


			except  Exception as msg:
				print("第 %s 张存储失败" %x)
				n +=1
			x+=1
			# print("第 %s 张图片保存完成"%x)
		print("总共失败 %s 张"%n)
		print("图片爬取完毕")

if __name__ =="__main__":
	# start =int(time.time())
	a = Get_image()
	# a.get_image()
	a.save_image()
	# alltime = int(time.time())-start
	# print(alltime)