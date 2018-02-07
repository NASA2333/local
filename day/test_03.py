#错误处理
# try:
# 	num = int(input("请输入一个数字"))
# except ValueError as msg:
# 	print("数字输入错误")
# # 	raise ValueError
# else:
# 	print("输入正确")
# finally:
# 	print("输入错误")
try:
	a = open(r"d:\test1.txt")
except IOError as msg:
	print("打开失败")
