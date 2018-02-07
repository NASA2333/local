# import fmovice
#
# print(fmovice.Search_Movice("长城"))

# from selenium import webdriver
#
# driver = webdriver.Chrome()
# driver.get("http://www.baidu.com")
# a =driver.current_window_handle
# b = driver.window_handles
# print(type(a))
# print(type(b))
from selenium import webdriver
from time import sleep
# try:
# 	num = int(input("请输入一个数字"))
# except ValueError as msg:
# 	print("数字输入错误")
#
#

import time,datetime

date = "2017-4-15"
now_time= time.strftime("%Y-%m-%d",time.localtime())
now = now_time.split("-")
ago =date.split("-")

year_1 =now[0]
month_1=now[1]
day_１ = now[2]

year_2 =ago[0]
month_2=ago[1]
day_2 = ago[2]

d1 = datetime.datetime(int(year_1),int(month_1),int(day_１))
d2 =datetime.datetime(int(year_2),int(month_2),int(day_2))

print((d1-d2).days)