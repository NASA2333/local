# from python.read_excel import Read
import time
import datetime
from selenium import  webdriver
from selenium.webdriver.common.action_chains import ActionChains

# a =Read(r'E:\data\testdata.xls')
# print(a.read_cell(1,1))
# # print(a.table)
print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))
# print(datetime.datetime())
# fp = r"C:\Users\wangal0425\AppData\Roaming\Mozilla\Firefox\Profiles\r3vt8ulr.default"
# # fpprofile = webdriver.FirefoxProfile(fp)
# # ob = webdriver.Firefox(fpprofile)
# ob = webdriver.Chrome()
# ob.maximize_window()
# ob.get("http://fs.mmh5.cn/game/7/hrdt/index.html?canalId=hrdt6")
# time.sleep(8)
# a =ob.find_element_by_tag_name('canvas')
# print(a)
# time.sleep(4)
# # ActionChains(ob).move_by_offset(303,59).send_keys('测试').perform()
# # ActionChains(ob).move_to_element_with_offset(a,210,1025).send_keys('test测试').perform()
# ActionChains(ob).move_to_element_with_offset(a,0,0).click().perform()

