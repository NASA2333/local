# import requests
# import time
# import json
#
# time = int(time.time() * 1000)
# headers = {"Connection": "keep-alive", "number": "CD00001", "timestamp": str(time), 'api-version': '1'}
#
# data = {'cardId':'000003531975','deptId':'13','doctorId':'6417','scheduleId':'74295','date':'2017-11-30','period':'all'}
# print(type(data))
# r = requests.post(' http://139.199.206.91:8087/registration/lock',json=data,headers=headers)
# print(r)
# t = r.json()
#
# g = json.dumps(t, ensure_ascii=False).encode('iso-8859-1').decode('utf-8')
# print(g.txt)
# print(g)
#
#
#
#
#
# assert 'msg' in g

#
import  xlrd,time,datetime

table =xlrd.open_workbook(r'D:\Runtime.xlsx').sheet_by_index(0)

nrows = table.nrows
# def change_timestamp():
    # for i in range(1,nrows):
    #     timestamp=table.cell(i,1)
    #     newtimestamp=str(timestamp)
	#
    #     a = newtimestamp.split(":")[1]     #转换，取值
    #     c =float(a)							#转换格式    不知道为啥一定要这步，不能直接在下面转换中直接float(a)
	#
    #     timeArray = time.localtime(c)
    #     otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    #     print(otherStyleTime)
	#
    #     # print(type(newtimestamp))
    #     # print(num)


