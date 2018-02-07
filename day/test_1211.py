import requests,re,urllib.request,os

# urls =r"https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord=%E7%A5%9E%E5%A5%87%E5%A5%B3%E4%BE%A0%0A&" \
# 	  r"cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&" \
# 	  r"word=%E7%A5%9E%E5%A5%87%E5%A5%B3%E4%BE%A0%0A&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&pn=990&rn=30&gsm=7bc&1512972323692="
# a =requests.get(url=urls)
# b = a.text
# c = re.findall(r'(?<=middleURL":").+?(?=",\s{4}"la)',b)
# print(c)
# #
# a = requests.get(r"https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&"
# 				 r"queryWord=%E6%A3%AE%E6%9E%97&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&word=%E6%A3%AE%E6%9E%97&"
# 				 r"s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&pn=240&rn=30&gsm=1e&1512958009190=")

# a.encoding('utf-8')
# b = a.text
# print(b)
# c = a.json()
# d = c['data'][0]
# print(d)
# if d :
# 	print("yes")
# else:
# 	print("No")
# print(d is False)
# print(re.search())
# c = re.findall(r'(?<=middleURL":").+?(?=",\s{4}"la)',b)
# print(c)
# print(len(c))

# x = 60
# for i in c:
# 	urllib.request.urlretrieve(i,os.path.join(r"D:\baidu_image\testone","%s.jpg"%x))
# 	x+=1



# c= re.findall(r"(\bhttps:.+?jpg)",b)
# x =set(c)
# print(len(x))
# z = "cbdfcsadw"
# print(re.findall('c',z))

# with open(r'D:\test6.html','w',encoding="utf-8") as f:
#     f.write(a.text)

# z = {'a':50,'b':10}
# print(z)
# z['a']+=30
# print(z)
datas = input("请输入你想要搜索的关键词：")
prmas ={"tn":"resultjson_com","ipn":"rj","ct":201326592,"fp":"result","queryWord":datas,"cl":2,"lm":-1,"ie":"utf-8","oe":"utf-8",
			"st":-1,"ic":0,"word":datas,"face":0,"istype":2,"nc":1,"pn":30,"rn":30,"gsm":"7bc"}

urls =r'https://image.baidu.com/search/acjson'
a = requests.get(url=urls,params=prmas)
b = re.findall(r'(?<=middleURL":").*?(?=",)',a.text)
print(b)
print(len(b))