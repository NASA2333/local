from bs4 import BeautifulSoup
import time,requests,re,os,sys

class GetQiuBai():
	def get_message(self):
		self.dates = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
		parms = {'user_time':str(self.dates),'version':'2017-09-04 14:36',"protocol":'https'}
		url_1 =r'https://www.qiushibaike.com/text/page'
		num =1
		while num<=20:
			url=url_1+'/'+str(num)
			r = requests.get(url=url,params=parms)
			a = requests.get(url='https://www.qiushibaike.com/text/')
			soup = BeautifulSoup(a.text,"html.parser")
			self.get_num(a.text)
			d =soup.find_all(class_="content")
			for i in d:
				x = i.contents[1].text
				self.write(x)
				self.write("点赞:"+self.numlist[d.index(i)][0]+'\t\t'+"留言:"+self.numlist[d.index(i)][1])
				# self.write('\t\t'+"留言:"+self.numlist[d.index(i)][1])
			num +=1

	def get_num(self,source):
		z = re.findall(r'(?<=number">).*(?=</i>)',source)
		self.numlist=[z[x:x+2] for x  in range(0,len(z),2) ]
		return self.numlist

	def write(self,i):
		path1 = self.dates.replace(":","")+'.txt'
		c =os.path.join(r"D:\baidu_image\QiuBai",path1)
		a = open(c,'a')
		a.write(i+'\n')
		a.close()

if __name__ =="__main__":
	a =GetQiuBai()
	a.get_message()


