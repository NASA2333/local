# import urllib.request,urllib.error,urllib.parse
#
#
#
# import requests
# import json
#
# payload = {
#     "password":"123456",
#     "p_version":"1",
#     "phone_number":"18677470000",
#     "terminal_type":"iPhone8,1",
#     "terminal_serial":"BE50766E-8A67-46AE-A5FB-FE63585EBA1F"
#     }
# header = {'Content-Type': 'application/json'}
#
# url = "https://172.16.3.121/api/aaa/login/fm"
#
# r_post = requests.post(url, json=payload,headers = header,verify=False)
# print(r_post.json())

# print("\t\t欢迎使用双球球选号系统\n请选择你想要执行的操作：\na\t新增\nb\t打印\nc\t删除\nd\t修改\ne\t退出")
# a =['1','2','3','4']
# b = [1,2,3,4]
# # dict = {}
# # for index,num  in enumerate(a):
# #     dict[a[index]] =b[index]
# #
# # print(dict)
#
# dict1 = {}
#
# for i in range(len(a)):
#     dict1[a[i]] =b[i]
# print(dict1)
#
#
#
# dict2 ={}
# print(dict(zip(a,b)))
#
# for  i in b:
#     dict2[a[i-1]] =b[i-1]
#
# print(dict2)


keys = ['a','b','c']
values=[1,2,3,4,5,6]
values[2],values[-1] =values[-1],values[2]
print(values)
# dict={}
# for i in values:
# 	dict[keys[i-1]]=values[i-1]
# print(dict)
# #print(dict(zip(keys,values)))
