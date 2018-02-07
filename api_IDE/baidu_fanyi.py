'''
百度翻译接口，自动判断输入的语种进行翻译，其他语种默认翻译为中文
中文，默认翻译为英文
语种库接口还没看

'''
import requests,os

class trans():
	def __int__(self):
		# self.intstr = ''
		pass
	def getlan(self,s):
		'''获取语种'''
		parms ={'query':s,'Content-Type':'application/json'}
		r= requests.post(r'https://fanyi.baidu.com/langdetect',data =parms,verify=False)
		return r.json()['lan']

	def choice(self,s):
		if self.getlan(s) =='zh':
			return self.zh2en(s)
		else:
			return self.oth2zh(s)

	def zh2en(self,s):
		'''
		中文至英文
		'''
		parms ={'from':'zh','to':'en','query':s,'simple_means_flag':'3','Content-Type':'application/json'}
		r= requests.get(r'http://fanyi.baidu.com/v2transapi',params =parms)
		# print(str(r.content,'utf-8'))
		# print(r.json())
		# print(r.json()['trans_result']['data'][0]['result'][0][1])
		return (r.json()['trans_result']['data'][0]['result'][0][1])



	def oth2zh(self,s):
		'''其他语种翻译中文'''
		parms ={'from':self.getlan(s),'to':'zh','query':s,'simple_means_flag':'3','Content-Type':'application/json'}
		r= requests.get(r'http://fanyi.baidu.com/v2transapi',params =parms)
		return  (r.json()['trans_result']['data'][0]['result'][0][1])

	def main(self):
		inputs = input("请输入你想要翻译的词语")
		return self.choice(inputs)

if __name__ =="__main__":
	# a = trans()
	# print(a.main())

	print(os.path.dirname(os.getcwd()))
	print(os.getcwd())
	print(os.path.dirname(__file__))
	print(os.path.split(os.path.realpath(__file__))[0])