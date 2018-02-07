import requests,json

header = {'Content-Type': 'application/json',}
data = {"keyword":"978-3-0016-0001-7"}
r= requests.post(url='http://pcms.pdri.t:8070/pdri/pcms/website/v102/search/pdri?flag=required&langCode=ZH_CN&pageIndexSize=10&pageNo=1&pageSize=3',
				 headers =header,data =json.dumps(data))
print(r.text)