import time
import requests
import json
import hashlib
# # 172.16.5.162
# ####2.4.1   2.4.1.获取MPR注册中心系统验证key和systemId的方法
#
'''
time = int(time.time()*1000)
time1 = str(time)
print(time)

header = {'publisherId':'14759770794273922','timestamp':str(time)}
# r= requests.get(url='http://172.16.5.162:8080/mpr/portal-mcrs-openapi/mvc/mprcode/getkey',params={'publisherId':1386833104009,'timestamp':time1})
r= requests.get(url='http://172.16.5.162:8080/mpr/portal-mcrs-openapi/mvc/mprcode/getkey',headers=header)
print(r.url)
print(r.text)
t=r
print(r.json().get('key'))
print(type(r.json().get('key')))

# http://172.16.5.162:8080/mpr/portal-mcrs-openapi/mvc/mprcode/exportExcel_1
'''


# m2 =hashlib.md5()
# scr = 'c1a5b02cf4b04d1f8da77cd2c70a3c21'+str(time)
# print(scr)
# m2.update(scr.encode('utf-8'))
# ticket = m2.hexdigest()
# print(ticket)
#
# header= {'publisherId':'1386833104009','timestamp':time1,'systemId':'c1a5b02cf4b04d1f8da77cd2c70a3c21','ticket':ticket}
# params = {'publisherId':'1386833104009','publicationType':'1','CodeType':'1','statusScope':'manager','startRow':'1','endRow':'10','startTime':'2017,05,01','endTime':'2017,07,01',
# 		  'mprStatus':'5','bookNameCn':'青年文摘1','langId':'chi','clcId':'101!-!102','mprCode':'0000025076'
# 		  }
#
# r= requests.get(url='http://172.16.5.162:8080/mpr/portal-mcrs-openapi/mvc/mprcode/exportExcel_1',params=params,headers=header)
# print(r.status_code)
# print(r.url)
# print(r.text)
# print(r.content)

# http://im_manager.mpr.d:8080/mpr/portal-mcrs-openapi/mvc/news/all
'''
###2.1.22.1.2.MPR用户/账号状态查询的方法----rms系统(接口不通）

r= requests.post(url="http://172.16.5.162:8080/mpr/portal-mcrs-openapi/mvc/api-publisher/status",data={'accountId':14969738131211506})
print(r.text)
print(r.content)

'''
##2.1.3.MPR用户/账号状态查询的方法
'''
r= requests.get(url='http://172.16.5.162:8080/mpr/portal-mcrs-openapi/mvc/api-publisher/account/status',params={'accountId':14969738131211506})
print(r.text)
'''
# 2.1.4.获取省份信息的方法
'''
r= requests.get(url='http://172.16.5.162:8080/mpr/portal-mcrs-openapi/mvc/api-publisher/provinces')
print(r.content.decode('utf-8'))

'''
###2.1.5.获取注册的集团信息的方法
"""
r= requests.get(url='http://172.16.5.162:8080/mpr/portal-mcrs-openapi/mvc/api-publisher/groups')
print(r.content.decode('utf-8'))
"""
#  2.1.6.下载注册登记表 - word文档    失败，data查询失败
'''
r =requests.get(url='http://172.16.5.162:8080/mpr/portal-mcrs-openapi/mvc/api-publisher/downLoad',params={'applyusermail':4957010019904287})
print(r.content.decode('utf-8'))
'''




#
'''
# 2.2.1   2.2.1.获取新闻列表的方法
# params = {"pageNo":1,"pageSzie":'10'}
# r=requests.get(url="http://172.16.5.162:8080/mpr/portal-mcrs-openapi/mvc/news/all",params=params)
# print(r.text)
# print(r.url)
# print(r.json().get('respMsg'))
#
'''


#2.3.1.获取MPR元数据详情的方法 - 根据MPR前置码及指定发行商
'''
r= requests.get(url ='http://172.16.5.162:8080/mpr/portal-mcrs-openapi/mvc/publication/querySpecifyPublicationByMprcode',params={'mprCode':'0000025023','publicationType':'3'})
print(r.content.decode('utf-8'))
'''
##2.3.2.根据前置码修改图书信息，同时生效图书信息的方法
'''
# data = {'bookNameCn':'测试修改书名','author':'','isbn':'','editing':'hwq','publicationContentSummary':'修改描述','wordage':'','languageCode':'','mprCode':'0000025463','publicationType':'1'}
data = {'bookNameCn':'测试修改书名','editing':'这个也要改吗','publicationContentSummary':'修改描述','mprCode':'0000025463','publicationType':'1'}
# header = {'Content-Type': 'application/x-www-form-urlencoded'}
r = requests.post(url='http://172.16.5.162:8080/mpr/portal-mcrs-openapi/mvc/publication/updatePublicationByMprcode',data=data)
print(r.content.decode('utf-8'))
'''

#2.3.3.查询出版物列表信息的方法(通过指定发行商ID编号)   请求失败
'''
data ={'pubicationType':'1','specifyPublisherId':'14759770794273922','specifyPublisherType':'0','isPar':'true'}
r = requests.post(url='http://172.16.5.162:8080/mpr/portal-mcrs-openapi/mvc/publication/queryPublicationList',data=data)

print(r.content)

'''

#2.3.4.查询制作中或已发布的出版物信息(通过出版物ID编号)的方法
'''
data = {'pubicationType':'1','publicationId':'1'}
r= requests.post(url='http://172.16.5.162:8080/mpr/portal-mcrs-openapi/mvc/publication/queryPublicationById',data=data)

print(r.content)

'''

##2.4.17.获取mpr元数据接口-条件：书名  Maker
'''
params ={'bookNameCn':'世界文化与自然遗产-图书','codeType':'2','publisherType':'0','publisherId':'14759770794273922'}
r= requests.get(url = 'http://172.16.5.162:8080/mpr/portal-mcrs-openapi/mvc/mprcode/queryBookName',params =params)

print(r.content.decode('utf-8'))
'''






#
##2.4.2 导出MPR前置码出版物列表的方法#
# http://im_manager.mpr.d:8080/mpr/portal-mcrs-openapi/mvc/mprcode/exportExcel_1

# t= int(time.time()*1000)
'''
time1 = str(int(time.time()*1000))
m2 =hashlib.md5()
scr = '722d50a9-28d4-4cba-b226-ca1f1115f37d'+ time1
m2.update(scr.encode('utf-8'))
ticket = m2.hexdigest()
header = {'publisherId':'1386833104009','timestamp':time1,'ticket':ticket,'systemId':'ed480f03-c9f0-4612-a23b-afc2c2c8acc2'}
'''
'''
# params = {'publisherId':'1386833104009','publicationType':'3','CodeType':'1','statusScope':'manager','startRow':'1','endRow':'10','newspaperNameCn':'测试申请报纸4','newspaperType':'1!-!1','mprCode':'0000025869'}
# ?publisherId=14562849475323630&publicationType=4&codeType=1&statusScope=apply&startRow=1&endRow=10&audioNameCn =音像&mprCode=0000016341
params ={'publisherId':'14562849475323630','publicationType':'4','codeType':'1','statusScope':'apply','startRow':'1','endRow':'10','audioNameCn':'音像','mprCode':'0000016341'}
r = requests.get(url ='http://172.16.5.162:8080/mpr/portal-mcrs-openapi/mvc/mprcode/exportExcel_1',params=params,headers=header)
print(r.url)
print(r.text)

#
#
# #####2.4.3.前置编码申请服务的方法
# http://im_manager.mpr.d:8080/mpr/portal-mcrs-openapi/mvc/mprcode/apply
'''
data2 ={
    "publicationType": "2",
    "periodical_metadata": {
        "periodicalNameCn": "期刊接口测试专用",
        "periodicalRecord": "eng",
        "periodicalType": "1",
        "pageNumber": "111",
        "expectUseSize": "132",
        "fascicle": "1",
        "cn": "12,2346,HT",
        "codeType": "1",
        "issn": "1234-5673",
        "releaseDate": "2017-12-01",
        "periodicals": "11",
        "infoIntegrity": 1,
        "stopPublishYear": "2019",
        "specifyPublisherType": "0",
        "specifyPublisherId": "14750239901509314",
        "specifyPublisherName": "北京双语时代广告有限公司",
        "classNumber": "E",
        "priceType": "11.3,CNY",
        "organizers": "殇",
        "publishCountry": "CN",
        "competentOrg": "殇",
        "size": "123,123",
        "foundedYear": "2017",
        "format": "123,123,123"
    }
}
data1 ={
  "publicationType": "3",
  "newspaper_metadata": {
    "newspaperNameCn": "test book01",
    "newspaperType": "123",
    "newspaperCn": "123",
    "versionNumber": "132",
    "releaseDate": "2015-12-01",
    "releaseArea": "123",
    "issues": "111",
    "infoIntegrity": 1,
    "isTop": 1,
    "specifyPublisherType": "111",
    "specifyPublisherId": "1",
    "specifyPublisherName": "test",
    "fascicle": "111",
    "bookmaker": "111",
    "publishCountry": "123",
    "organizers": "123",
    "langId": 11,
    "competentOrg": "123",
    "keywords": "123",
    "domPubUnit": "123",
    "domEmailedCode": "123",
    "forPubUnit": "123",
    "forEmailedCode": "123",
    "priceType": "11.3,CNY",
	"codeType": "1",
    "colors": "1"
  }
}




time1 = str(int(time.time()*1000))
m2 =hashlib.md5()
scr = '722d50a9-28d4-4cba-b226-ca1f1115f37d'+ time1
m2.update(scr.encode('utf-8'))
ticket = m2.hexdigest()

data = {'publicationType':'3',
        'newspaper_metadata':{'newspaperNameCn':'test接口报纸11',
                              'newspaperType':'1,1',
                              'newspaperCn':'12,1234',
                              'versionNumber':'16',
                                'releaseDate':'2017-12-01',
                              'releaseArea':'2','issues':'18',
                              'infoIntegrity':'1','isTop':'1',
                                 'specifyPublisherId':'1386833104009',
                              'specifyPublisherName':'天朗闻听（北京）图书有限公司',
                              'specifyPublisherType':'0','fascicle':'1',
                                'bookmaker':'122','publishCountry':'1',
                              'organizers':'1212',
                              'langId':'ger',
                              'competentOrg':'122',
                              'keywords':'测试关键字',
                                'domPubUnit':'国内发行单位',
                              'domEmailedCode':'国内邮发代码',
                              'forPubUnit':'国外邮发单位',
                              'forEmailedCode':'国外邮发代码',
                              'priceType':'20,CNY',
                               'codeType':'1',
                              'colors':'1'
                }
        }
#

header = {'publisherId':'1386833104009','timestamp':time1,'ticket':ticket,'systemId':'469b235f-3ef1-4472-9892-055af1ede259'}
print(type(data1))
r = requests.post(url='http://172.16.5.162:8080/mpr/portal-mcrs-openapi/mvc/mprcode/apply',headers=header,json=data1)

s= requests.post
print(r.status_code)
print(r.url)
# print(r.history)
print(r.url)
# print(r.headers)
print(r.text.encode('utf-8'))
print(r.content)
# print(r.json().get('respcode'))





#   2.4.8   .下载MPR授权文件的方法
'''
time1=str(int(time.time()*1000))
header = {'publisherId':'1386833104009','timestamp':time1}
# r= requests.get(url='http://172.16.5.162:8080/mpr/portal-mcrs-openapi/mvc/mprcode/getkey',params={'publisherId':1386833104009,'timestamp':time1})
r= requests.get(url='http://172.16.5.162:8080/mpr/portal-mcrs-openapi/mvc/mprcode/getkey',headers=header)
# print(r.content)
systemId = r.json().get('systemId')
print(str(systemId))
key = r.json().get('key')
# print(key)
# print(time1)
scr =key+time1
m2 = hashlib.md5()
m2.update(scr.encode('utf-8'))
ticket = m2.hexdigest()
# m2 =hashlib.md5(scr.encode('utf-8'))
#
#
# # m2.update(scr)
# ticket = m2.hexdigest()
# print(ticket)

# http://im_manager.mpr.d:8080/mpr/portal-mcrs-openapi/mvc/mprcode/getAuthFileUrl
header1 ={'publisherId':'1386833104009','timestamp':time1,'ticket':ticket,'systemId':systemId}
params = {'publicationType':'1',"mprCode":'0000025528'}
re = requests.get(url='http://172.16.5.162:8080/mpr/portal-mcrs-openapi/mvc/mprcode/getAuthFileUrl',params=params,headers=header1)
print(re.url)
print(re.content.decode('utf-8'))
'''

###   2.4.7.获取渠道的的方法 - （获取出版社或书商接口）

#http://im_manager.mpr.d:8080/mpr/portal-mcrs-openapi/mvc/mprcode/getVendorInfo


# r= requests.get(url='http://172.16.5.162:8080/mpr/portal-mcrs-openapi/mvc/mprcode/getVendorInfo',headers=header,params={'typeId':'3','clientType':'1'})
# print(r.text)
#

# https://localhost:8443/mpr/portal-mcrs-openapi/mvc/mprcode/getInfo
'''
data ={'publicationType':1}
##2.4.15
r= requests.post(url='https://172.16.5.162:8443/mpr/portal-mcrs-openapi/mvc/mprcode/getInfo',headers=header,params=data,verify=False)
print(r.text)
print(r.url)
'''






















# from datetime import *
#
# print(datetime.today()+timedelta(2))
# import threading
# from time import sleep
# def a():
#     # x= 0
#     # while True:
#     #     x= x+1
#     #     print("%d %s\n"%(x,'loop'))
#     #     sleep(3)
#     for i in range(4):
#         i = i+1
#         print("%d %s"%(i,'loop'))
#         sleep(3)
# def thd():
#     Threads=[]
#     for i in range(10):
#         t = threading.Thread(target=a)
#
#         Threads.append(t)
#         t.setDaemon(True)
#         # t.start()
#         print("%d %s"%(i+1,'child thread start'))
#         # t.join()
#         for t in Threads:
#             t.start()
#         for t in Threads:
#             # t.start()
#             t.join()
# if __name__=="__main__":
#     print("start up")
#     thd()
#     print("end !!!!")

# from selenium import webdriver
# import time
#
# ob = webdriver.Firefox()
# ob.get("https://106.75.103.25:8443/mpr/portal-mcrs-publisher/mvc/publisher/toLogin")
# ob.find_element_by_id("userName").send_keys('mpr_20130008')
# ob.find_element_by_id("passWord").send_keys('aaaaaa')
# ob.find_element_by_name("validCode").send_keys('8888')
# time.sleep(5)
# ob.find_element_by_class_name('btn').click()
#
# time.sleep(3)
# ob.find_element_by_class_name("forData2").click()
# time.sleep(3)
