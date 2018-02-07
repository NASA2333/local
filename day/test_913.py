class foo():
	'''填写描述'''
	def set(self):
		pass

print(foo().__doc__)

a = iter([1,2,3,4,5,6,7])
for i in range(5):
	print(next(a))