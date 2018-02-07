import os
a =os.getcwd()
# print(os.path.dirname())
print(os.path.dirname(os.getcwd()))					#上级目录
print(os.getcwd())									#当前目录
print(a+r'\cwe')
print(os.path.abspath('..\data'))					#上级目录下的其他路径
print('./case')