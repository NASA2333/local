import requests,re,os,urllib.request,time


# r = requests.get(url=r"https://cn.bing.com/?",verify =False)
# txt = r.text
# a = re.findall('(?<=g_img=\{url: ").*?(?=\")',txt)
# # xpath = os.path.join("https://cn.bing.com/",a[0])
# xpath = "https://cn.bing.com/"+a[0]
# print(xpath)
#
# path1=r"D:\baidu_image\bing"
# if not os.path.exists(path1):
# 	os.makedirs(path1)
# else:
# 	urllib.request.urlretrieve(xpath,os.path.join(path1,(str(int(time.time())))+".jpg"))

a = urllib.request.urlretrieve('https://images.ioliu.cn/bing/Snowflake_EN-GB8186875426_1024x768.jpg',r"D:\tt.jpg")