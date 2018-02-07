import  requests,unittest,time,xlrd,json
from ddt import  ddt,data

requestdata = []   #请求参数

class Finddata():
	xls  =xlrd.open_workbook(r'D:\python\test\data\api_data.xls').sheet_by_index(0)
	nrows = xls.nrows

	for i in range(1,nrows):
		# r ={}
		a =xls.row_values(i)
		# r['casename'] =a[0]
		# r['url']=a[1]
		# r['header']=eval(a[3])
		# r['data']=json.dumps(eval(a[4]))
		# r['asser'] =a[6]
		requestdata.append(a)
		# requestdata.append(r)

@ddt
class Testapi(unittest.TestCase):
	def setUp(self):
		pass
	def requ(self,url,header,datas,asser):
		r = requests.post(url,headers =header,data=datas)
		self.assertIn(asser,r.text)

	@data(*requestdata)
	def test_api(self,data):
		# print(data['casename'])
		# self.requ(data['url'],data['header'],data['data'],data['asser'])
		print(data[0])
		self.requ(data[1],eval(data[3]),json.dumps(eval(data[4])),data[6])
	def tearDown(self):
		pass

