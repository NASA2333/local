###装饰器
def dress(func):
	def result():
		print("开始测试之前.....\n.")
		func()
		print("\n测试结束之后......")
		return  func()

@dress
def test_01():
	print("第一次测试")

@dress
def test_02():
	print("第二次测试")

def test_03():
	print("第三次测试")

def test_04():
	print("第四次测试")

def test_05():
	print("第五次测试")

def test_06():
	print("第六次测试")



test_01()
test_02()
test_03()
test_04()
test_05()
test_06()
