import  requests
url = 'http://dict.youdao.com/jsonapi'

##ljust()   左对齐   rjust()右对齐    center() 居中
parms = {'q' :"参考"}

r = requests.get(url =url,params=parms)
#,'dogui':'json','le':'eng'
# print(r.json()['ce']['word'][0]['trs'][0]['tr'][0]['l']['i'][1]['#text'])
a =r.json()['ce']['word'][0]['trs']
for i in a:
	# print(i['tr'][0]['l']['i'][1]['#text'],i['tr'][0]['l']['#tran'])
	# print("{0}\t{1}".format(i['tr'][0]['l']['i'][1]['#text'],i['tr'][0]['l']['#tran']).ljust(50))
	print((i['tr'][0]['l']['i'][1]['#text']).ljust(20),(i['tr'][0]['l']['#tran']).ljust(20))