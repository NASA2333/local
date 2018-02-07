import os,sys,re

# a = os.path.dirname(__file__)
# print(a)
# print('11111')
config_name ="test_1815.py"
if hasattr(sys, "frozen"):
	application_path = os.path.dirname(sys.executable)
	xpath = os.path.join(application_path, config_name)
# else:
# 	# application_path = os.path.dirname(__file__)
# 	xpath = os.path.dirname(__file__)

# 	print(xpath)
# print('11111')

# print("\033[1;32;40mgreen right is on...\033[0m")
# print("\033[1;30;41mred right is on...\033[0m") #红灯
# b = "导出文件 %s 内容正常"%os.path.dirname(__file__)
# print("\033[1;30;42m\033[0m")

x = ['MPRX/license.xml', 'MPRX/MPRCode_Resources.xml', 'MPRX/ISLISearchEx/SrcFragmentDesc.xml',
	 'MPRX/ISLISearchEx/SrcFragmentImage/00101_00.png', 'MPRX/ISLISearchEx/SrcFragmentImage/00101_01.png',
	 'MPRX/ISLISearchEx/SrcFragmentLicense.xml', 'MPRX/ExtendInfo.xml', 'MPRX/ExtendInfo/001.jpeg',
	 'MPRX/ExtendInfo/002.jpeg', 'MPRX/ExtendInfo/003.jpeg', 'MPRX/ExtendInfo/004.jpeg', 'MPRX/ExtendInfo/005.jpeg',
	 'MPRX/ExtendInfo/006.jpeg','MPRX/MultiMedia/11 - 副本###02477964812149ab2b8eeddd3b424530.jpg',
	 'MPRX/MultiMedia/11 - 副本###02477964812149ab2b8eeddd3b424530.jpg',]
# b = "".join(x)
# print(b)
# if re.findall(r"MPRX/MultiMedia",b):
# 	print("True")
# else:
# 	print("没有")

print(sys.path)