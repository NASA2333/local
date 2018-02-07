from ddt import  ddt,data
import unittest,requests,xlrd,json,time,hashlib

requestdata =[]

class get_head():
	time = int(time.time()*1000)
	time1 = str(time)
	header = {'publisherId':'14994769405862912','timestamp':str(time)}
	r= requests.get(url='http://172.16.5.162:8080/mpr/portal-mcrs-openapi/mvc/mprcode/getkey',headers=header)
	key = r.json().get('key')
	systemid = r.json().get('systemId')					#获取key、systemid

	m2 =hashlib.md5()
	scr = key+str(time)
	m2.update(scr.encode('utf-8'))
	ticket = m2.hexdigest()

	xls  =xlrd.open_workbook(r'D:\python\test\data\api_data.xls').sheet_by_index(1)
	nrows = xls.nrows
	for i in range(1,nrows):
		a =xls.row_values(i)
		#组合header（可以写成单独函数）
		head = {}
		head['publisherId'] ='14994769405862912'
		head['timestamp']=time1
		head['ticket']=ticket
		head['systemId']=systemid
		a.insert(3,head)
		del a[4]
		print(a)
		requestdata.append(a)


@ddt
class Testapi_mcrc(unittest.TestCase):
	def setUp(self):
		pass
	def requ(self,url,header,datas,asser):
		r = requests.post(url,headers =header,json=datas)
		time.sleep(2)
		self.assertIn(asser,r.text)


	@data(*requestdata)
	def test_api(self,data):
		print('case name:',data[0])
		self.requ(data[1],data[3],eval(data[4]),data[6])

	def tearDown(self):
		pass
