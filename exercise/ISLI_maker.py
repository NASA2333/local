import unittest

from test.exercise import ISLI_login


class Maker_mpr(unittest.TestCase):
	def setUp(self):
		# self.driver = base.BasePage
		ISLI_login.Beta().setUp()
		ISLI_login.Beta().test_login_success()


		self.driver.click(("css",'img[height="150px"]'))

	def test_1(self):
		pass
	def tearDown(self):
		# self.driver.close()
		pass
if __name__=="__main__":
	unittest.main()