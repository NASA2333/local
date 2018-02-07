from selenium import  webdriver
ob = webdriver.Firefox()
ob.get("http://www.baidu.com")
ob.find_element('css','#kw').send_keys("111")
