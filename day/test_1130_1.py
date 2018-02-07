from selenium import  webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
ob =webdriver.Chrome()
# try:
ob.get(r"https://172.16.3.251:9443/#/systemStart")
time.sleep(2)
ob.find_element_by_css_selector('.for_system>span').click()

ob.find_element_by_id("loginName").send_keys('xitest025@163.com')
ob.find_element_by_id('loginPassword').send_keys('a123456')
ob.find_element_by_css_selector('button.btn-primary').click()
time.sleep(1)
a = ob.find_element_by_css_selector('.soft_link>li:nth-child(4)>div>a')
b = ActionChains(ob).move_to_element(a).click().perform()

# ob.find_element_by_css_selector('.soft_link>li:nth-child(4)>div').click()
time.sleep(5)
ob.switch_to_alert().text()


# except Exception as msg:
# 	ob.close()


