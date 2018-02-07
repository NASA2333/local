import unittest
import os
import time
import HTMLTestRunner
def run_all():
	testunit = unittest.TestSuite()
	discover = unittest.defaultTestLoader.discover(start_dir=test_dir,
												   pattern="test*.py",
												   top_level_dir=None)
	for i in discover:
		for test_case in i:
			testunit.addTest(test_case)
	return testunit

if __name__=="__main__":
	test_dir =r'.'
	now = time.strftime("%Y-%m-%d %H_%M_%S",time.localtime(time.time()))
	filename = 'D:\python\\test\\api\\'+now+"resut.html"

	print(filename)
	fp = open(filename,'wb')
	runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
										   title="ISLI_RA测试报告",
										   description="用例执行情况")
	runner.run(run_all())
	fp.close()
