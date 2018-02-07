'''
http://172.16.3.22:7081/bizcompetitor/api/publisher/detail?publisherUuid=14994769405862912&platform=%E6%B3%9B%E5%AA%92
'''

###友商系统获取标签
import requests
cook = dict(JSESSIONID="1275212A1471B7F2CDF23D7633AB5291",logoutUrl="https%3A%2F%2F172.16.3.48%3A9443%2F%23%2Flogin%3FsoftwareId%3D32")
r = requests.get(r'http://172.16.3.22:7081/bizcompetitor/api/publisher/detail',params={'publisherUuid':'14994769405862912','platform':'泛媒'},
				 cookies =cook)
print(r.json())