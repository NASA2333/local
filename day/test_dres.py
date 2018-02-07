import logging
def output(func):

	def wrapper():
		print("开始测试装饰器：")
		return func()
	return wrapper

@output
def foo():
	print("I am foo")

foo()






