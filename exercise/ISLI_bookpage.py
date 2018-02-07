from python import  base

page_url = r"https://172.16.5.161:8443/mpr/portal-mcrs-perecode/mvc/bookportal/bookApplyPortal?codeType=1&mcrs=V1.00001.P0TALO.4"

class bookpage(base):
	#定位器 页面元素
	ISBN_1_loc =("css","div:nth-child(3)>")