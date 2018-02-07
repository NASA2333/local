"""

from selenium import  webdriver
ob = webdriver.Firefox()

ob.get(r'http://172.16.3.53:8080/isli/irms/workbench-provider/base/provider/toRegiste?loginUrl=http://172.16.3.52:8080/irap/web/navigation/toLogin')
ob.maximize_window()
ob.find_element_by_id('logo_file').send_keys(r'D:\snipaste_20170824_173115.png')
a = (1,2,3,4)
print(type(len(a)))
"""

####8-30  request
import requests
# r = requests.get(r'http://www.baidu.com')
# print(r.status_code,r.content,r.text,r.headers,r.json(),r.url,r.encoding,r.cookies,r.raw)
'''
r.status_code      响应状态码				r.content    解码后的响应			r.text    字符串形式响应
r.headers			响应头					r.url		获取utl					r.json()   json解码
r.cookies			获取cookie				r.raw		返回原始体
'''
help(requests)

