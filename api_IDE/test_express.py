import  requests

## 1

#快递查询
"""
# sing ='f37554aeae4647f387512126d8bec857'

# NO = input("请输入快递单号：") 			#220539186762
# parms = {'showapi_appid':'50068','showapi_sign':'f37554aeae4647f387512126d8bec857','com':"auto",'nu':NO}
# r =requests.get(r'http://route.showapi.com/64-19',params=parms,timeout = 10)
# print(r.json())



b = {'showapi_res_body':
					{'expSpellName': 'shentong', 'expTextName': '申通快递', 'status': 4, 'update': 1510804012743, 'mailNo': '220539186762', 'ret_code': 0, 'dataSize': 7,
 'updateStr': '2017-11-16 11:46:52', 'msg': '查询成功!', 'flag': True,
'data': [{'context': '深圳市 本人-已签收，感谢您选择申通快递，期待再次为您服务。', 'time': '2017-05-27 12:31:49'},
	{'context': '深圳市 广东宝安坪州营业厅(29611910、0755-29611045、29611840、)-陈汉林(15814453862)-派件中', 'time': '2017-05-27 09:46:33'},
	{'context': '深圳市 已到达-广东宝安坪州营业厅', 'time': '2017-05-27 08:55:58'},
	{'context': '深圳市 广东宝安公司-已发往-广东宝安坪州营业厅', 'time': '2017-05-27 07:00:02'},
	{'context': '深圳市 广东深圳中转部-已发往-广东宝安公司', 'time': '2017-05-27 02:18:36'},
	{'context': '深圳市 已到达-广东深圳中转部', 'time': '2017-05-26 22:42:43'},
	{'context': '深圳市 广东深圳罗湖市场一部(0755-82475888)-平剑(13631655977)-已收件', 'time': '2017-05-26 13:26:11'}],
'tel': '400-889-5543'}, 'showapi_res_error': '', 'showapi_res_code': 0}
z = b['showapi_res_body']['data']

print(b['showapi_res_body']['expTextName'],'\t',b['showapi_res_body']['msg'])

for i in z:
	print(i['context'],'\t',i['time'])
"""
#2电影排行
'''
parms = {'showapi_appid':'50068','showapi_sign':'f37554aeae4647f387512126d8bec857'}
r =requests.get(r'http://route.showapi.com/578-1',params=parms,timeout = 10)
print(r.json())
'''

#公交线路查询
##换程
# parms = {'showapi_appid':'50068','showapi_sign':'f37554aeae4647f387512126d8bec857','city':"深圳",'start_addr':'深大','end_addr':'南昌村'}
# r = requests.get(r'http://route.showapi.com/844-3',params=parms)
# print(r.json())

#线路
# parms = {'showapi_appid':'50068','showapi_sign':'f37554aeae4647f387512126d8bec857','city':"深圳",'busNo':'321'}
# r = requests.get(r'http://route.showapi.com/844-2',params=parms)
# print(r.json())

#站点
# parms = {'showapi_appid':'50068','showapi_sign':'f37554aeae4647f387512126d8bec857','city':"深圳",'station':'深圳大学'}
# r = requests.get(r'http://route.showapi.com/844-1',params=parms)
# print(r.json())

'''
{'showapi_res_body': {'ret_code': 0,
'busList':
[{'segList': [{'line_name': '338路(皇岗口岸-海上田园)', 'stats': '深大北门(1);南头;中南花园;中商花园;甲岸路口;西城上筑;金成名苑;宝安体育馆东;群贤花园;河东;西乡步行街;同仁妇科医院;西乡盐田;西乡客运站', 'end_stat': '西乡客运站', 'start_stat': '深大北门(1)'}]},
{'segList': [{'line_name': '旅游线路; 西乡客运站--丹竹头 06:30--20:30; 冷巴上车2元，分段收费，全程8元滨观光线(丹平人行天桥-西乡客运站)', 'stats': '科技园(1);深大北门(2);南头;西城上筑;金成名苑;群贤花园;西乡步行街;同仁妇科医院;西乡盐田;西乡客运站', 'end_stat': '西乡客运站', 'start_stat': '科技园(1)'}]},
{'segList': [{'line_name': '323路(百鸽笼地铁接驳站-西乡客运站)', 'stats': '科技园(1);南头;南头检查站;宝安交通运输局;裕安路口;上川路口;西乡路口;西乡人民医院;西乡立交;新安市场;大益广场;西乡客运站', 'end_stat': '西乡客运站', 'start_stat': '科技园(1)'}]},
{'segList': [{'line_name': '1号线[罗宝线](罗湖-机场东)', 'stats': '深大;桃园;大新;鲤鱼门(只开通A口);前海湾;新安;宝安中心;宝体;坪洲;西乡', 'end_stat': '西乡', 'start_stat': '深大'}]},
 {'segList': [{'line_name': '1号线(罗湖-机场东)', 'stats': '深大;桃园;大新;鲤鱼门;前海湾;新安;宝安中心;宝体;坪洲;西乡', 'end_stat': '西乡', 'start_stat': '深大'}]},
 {'segList': [{'line_name': '311路(莲塘(港莲路)-桃源居总站)', 'stats': '科技园(1);深大北门(1);南头;南头检查站;沁园公园;宝安交通运输局;创业天虹南;海滨广场;翻身实验学校;开屏花园;西乡径贝村;河东;西乡步行街;同仁妇科医院;大益广场', 'end_stat': '大益广场', 'start_stat': '科技园(1)'}]},
 {'segList': [{'line_name': 'M358路(宝鼎总站-桃源居总站)', 'stats': '科技园(1);南头;中南花园;中商花园;甲岸路口;西城上筑;金成名苑;宝安体育馆东;群贤花园;河东;西乡步行街;同仁妇科医院;大益广场', 'end_stat': '大益广场', 'start_stat': '科技园(1)'}]},
 {'segList': [{'line_name': '高峰专线72路(科技园公交总站-西乡大铲湾码头)', 'stats': '高科技中心;深南科苑立交北;科苑北;海能达大厦;北环朗山二号路口;方鼎华庭;中南花园;中商花园;甲岸路口;西城上筑;金成名苑;宝安体育馆东;群贤花园;河东;西乡步行街;西乡盐田大门', 'end_stat': '西乡盐田大门', 'start_stat': '高科技中心'}]},
 {'segList': [{'line_name': 'M433路(皇岗口岸-凤凰山路口)', 'stats': '科技园(1);南头;南头检查站;宝安交通运输局;创业天虹南;海滨广场;翻身小学;开屏花园;河东;西乡步行街;同仁妇科医院;西乡盐田;西乡客运站', 'end_stat': '西乡客运站', 'start_stat': '科技园(1)'}]},
 {'segList': [{'line_name': '高峰专线30路(红树湾公交总站-凤凰山森林公园)', 'stats': '科技园(1);南头;南头检查站;宝安交通运输局;创业天虹南;海滨广场;翻身小学;开屏花园;西乡径贝村;河东;西乡步行街;同仁妇科医院;西乡盐田;西乡客运站', 'end_stat': '西乡客运站', 'start_stat': '科技园(1)'}]}]}, 'showapi_res_code': 0, 'showapi_res_error': ''}
 '''


##新闻///地区
"""
parms = {'showapi_appid':'50068','showapi_sign':'f37554aeae4647f387512126d8bec857',}
r = requests.get(r'http://route.showapi.com/170-48',params=parms)
print(r.json())
"""

#PM2.5

"""
#单个城市监控
parms = {'showapi_appid':'50068','showapi_sign':'f37554aeae4647f387512126d8bec857','city':'深圳'}
r = requests.get(r'http://route.showapi.com/104-29',params=parms)
print(r.json())
"""
##排行
"""
parms = {'showapi_appid':'50068','showapi_sign':'f37554aeae4647f387512126d8bec857'}
r = requests.get(r'http://route.showapi.com/104-41',params=parms)
print(r.json())
"""

#Alexa查询			世界排名   国家排名

# url = input("请输入网址")
# parms = {'showapi_appid':'50068','showapi_sign':'f37554aeae4647f387512126d8bec857','name':url}
# r = requests.get(r'http://route.showapi.com/24-1',params=parms)
# print(r.json())


#实时IP代理查询接口
# parms = {'showapi_appid':'50068','showapi_sign':'f37554aeae4647f387512126d8bec857'}
# r = requests.get(r'http://route.showapi.com/22-1',params=parms)
# print(r.json())

# #网址查询
# parms = {'showapi_appid':'50068','showapi_sign':'f37554aeae4647f387512126d8bec857','n':'10','f':'1'}
# r = requests.get(r'http://route.showapi.com/594-3',params=parms)
# print(r.json())


#百度翻译

# instr =input("请输入想要翻译的词语：")
'''中译英'''
# parms ={'from':'zh','to':'en','query':instr,'simple_means_flag':'3','Content-Type':'application/json'}
# r= requests.get(r'http://fanyi.baidu.com/v2transapi',params =parms)
# # print(str(r.content,'utf-8'))
# print(r.json()['trans_result']['data'][0]['result'][0][1])

'''英译中'''
# parms ={'from':'en','to':'zh','query':instr,'simple_means_flag':'3','transtype':'enter','Content-Type':'application/json'}
# r= requests.get(r'http://fanyi.baidu.com/v2transapi',params =parms)
# # # print(str(r.content,'utf-8'))
# print(r.json())
# print(r.json()['trans_result']['data'][0]['result'][0][1])


'''判断语种'''
# parms ={'query':instr,'Content-Type':'application/json'}
# r= requests.post(r'https://fanyi.baidu.com/langdetect',data =parms,verify=False)
# print(r.json()['lan'])

# parms ={'from':'kor','to':'zh','query':instr,'simple_means_flag':'3','transtype':'enter','Content-Type':'application/json'}
# r= requests.get(r'http://fanyi.baidu.com/v2transapi',params =parms)
# # print(str(r.content,'utf-8'))
# print(r.json())
# print(r.json()['trans_result']['data'][0]['result'][0][1])



#台风最新坐标轨迹接口

# parms = {'showapi_appid':'50068','showapi_sign':'f37554aeae4647f387512126d8bec857'}
# r = requests.get(r'http://route.showapi.com/342-1',params=parms)
# print(r.json())

#bign桌面

parms = {'showapi_appid':'50068','showapi_sign':'f37554aeae4647f387512126d8bec857'}
r = requests.get(r'http://route.showapi.com/1377-1',params=parms)
print(r.json())

#网络热词  	http://route.showapi.com/313-1   /

# parms = {'showapi_appid':'50068','showapi_sign':'f37554aeae4647f387512126d8bec857','typeId':'661'}
# r = requests.get(r'http://route.showapi.com/313-2',params=parms)
# print(r.json())
# z= r.json()
# for i in z['showapi_res_body']['list']:
# 	print(i['name'],'\t',i['num'])