import time,os,requests,re,urllib.request,codecs
from bs4 import BeautifulSoup

class SaveImage():
	def __init__(self):
		self.about_list=[]
		self.numb_list =[]
		self.url_list =[]
		self.page = 1

	def get_request(self):

		parm = {'p':self.page}
		head = {"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
		"Accept-Encoding":"gzip, deflate, br",
		"Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7,ja;q=0.6",
		"Cache-Control":"no-cache",
		"Connection":"keep-alive",
		"Cookie":"likes=; Hm_lvt_667639aad0d4654c92786a241a486361=1513579806; Hm_lpvt_667639aad0d4654c92786a241a486361=1513580293",
		"Host":"bing.ioliu.cn",
		"Pragma":"no-cache",
		"Referer":"https://bing.ioliu.cn/?p=3",
		"Upgrade-Insecure-Requests":"1",
		"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36",
		}
		r= requests.get(r'https://bing.ioliu.cn',headers =head,params=parm)
		return r.content

	def get_about(self):
		about = self.get_request()
		soup =BeautifulSoup(about,"html.parser")
		about_txt = soup.select('.description')
		for i in about_txt:
			self.about_list.append(i.text)

		num_txt =soup.select('.ctrl')
		for i in num_txt:
			self.numb_list.append(i.text)
		url_txt= soup.select("img.progressive__img")
		for i in url_txt:
			# print(i)
			if '800' in i['data-progressive']:
				self.url_list.append(i['data-progressive'].replace('800x480','1920x1080'))
			else:
				self.url_list.append(i['data-progressive'].replace('1024x768','1920x1080'))

	def make_image(self):
		self.numb_list1 =[self.numb_list[i:i+3] for i in range(0,len(self.numb_list),3)]
		return self.numb_list1


	def save_image(self):
		path1 =r'D:\baidu_image\bing'
		while self.page <=55:
			# self.get_about()
			self.get_about()
			self.page+=1
		self.make_image()

		for i in range(len(self.url_list)):
			# name =re.findall('(?<=\)).*',self.about_list[i])
			name = re.findall('201.*',self.about_list[i])				#获取文件名
			if len(name) ==0:
				xpath =os.path.join(path1,"%s"%str(i))
			else:
				xpath =os.path.join(path1,name[0])
			if not os.path.exists(xpath):
				os.makedirs(xpath)
				x = os.path.join(xpath,"%s.jpg"%str(i))
				y = self.url_list[i]
				# print(y)
				opener=urllib.request.build_opener()
				opener.addheaders=[("User-Agent","Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36")]
				urllib.request.install_opener(opener)
				urllib.request.urlretrieve(url=y,filename=x)
				txt = codecs.open(os.path.join(xpath,"%s.txt"%str(i)),'a','utf-8')
				txt.write(self.about_list[i]+'\n')
				if len(self.numb_list1[i])==3:
					txt.write("查看：%s \t 喜欢：%s \t 下载：%s \t"%(self.numb_list1[i][0],self.numb_list1[i][1],self.numb_list1[i][2]))
				else:
					for j in self.numb_list1[i]:
						txt.write(j)
				txt.close()




if __name__ =="__main__":
	a = SaveImage()
	# print(a.url_list)
	a.save_image()
