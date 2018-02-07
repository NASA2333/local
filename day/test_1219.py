# a= ['http://images.ioliu.cn/bing/ReindeerLichen_EN-AU9289253828_1024x768.jpg', 'http://images.ioliu.cn/bing/Snowflake_EN-GB8186875426_1024x768.jpg', 'http://images.ioliu.cn/bing/MGRBerlin_EN-GB6734108494_1024x768.jpg', 'http://images.ioliu.cn/bing/TamarackCones_EN-AU12178466392_1024x768.jpg', 'http://images.ioliu.cn/bing/SeychellesCCSS_EN-AU10430664838_1024x768.jpg', 'http://images.ioliu.cn/bing/PlutoNorthPole_ZH-CN12213356975_1024x768.jpg', 'http://images.ioliu.cn/bing/Freudenberg_EN-AU11714819408_1024x768.jpg', 'http://images.ioliu.cn/bing/Gnomes_EN-AU13899110865_1024x768.jpg', 'http://images.ioliu.cn/bing/Jangothang_EN-AU12673032792_1024x768.jpg', 'http://images.ioliu.cn/bing/SiberianJay_EN-AU7327037586_1024x768.jpg', 'http://images.ioliu.cn/bing/FlightFest_EN-AU9045713592_1024x768.jpg', 'http://images.ioliu.cn/bing/SibeliusMonument_JA-JP8903164725_1024x768.jpg', 'http://images.ioliu.cn/bing/Snow_ZH-CN11178898651_1024x768.jpg', 'http://images.ioliu.cn/bing/MatusevichGlacier_EN-AU13620113504_1024x768.jpg', 'http://images.ioliu.cn/bing/AberystwythSeafront_EN-AU9268158003_1024x768.jpg', 'http://images.ioliu.cn/bing/Motherboard_EN-AU12641512843_1024x768.jpg', 'http://images.ioliu.cn/bing/SchwetzingenAerial_ZH-CN11628382780_1024x768.jpg', 'http://images.ioliu.cn/bing/PotashPonds_EN-AU13213047688_1024x768.jpg']
# for i in a:
# 	i.replace('_1024x768','_1920x1080')
# print(a[0])
# b ='http://images.ioliu.cn/bing/ReindeerLichen_EN-AU9289253828_1024x768.jpg'
# print(b.replace('_1024x768','_1920x1080'))
# c = [i.replace('_1024x768','_1920x1080') for i in a]
# print(c)
import codecs,re
a = '达特穆尔国家公园内的驯鹿地衣，英国 (© Ian Redding/Getty Images Plus)2017-12-19欧洲, 英国, 达特穆尔国家公园'
print(a)
# b = codecs.open(r"d:\11.txt",'a','utf-8')
# # b =open(r"d:\111.txt",'w')
#
# b.write(a)
# b.write('科学')
# b.close()
# print("\xa9")
# z =re.findall('(?<=[\),）]).*',self.about_list[i])
b = ["2017gsjijisj)gis jisjgisg ijisjf jisji ",
	 "gsighish)jisgjisjgisijgs",
	 "gshjighsigjhs）jigsjisjiji"]
print(re.findall('(?<=[\),u"）"]).*',b))