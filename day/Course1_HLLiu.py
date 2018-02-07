#coding:utf-8
'''这些个函数命名不改了吧，不知道改啥'''

import os
def printHelloWorld():
    print('hello world')
class My_class:
    def printHelloWorld2(self):
        print('hello world again')

if __name__=='__main__':

	num = input('输入你喜爱的一个数字:')
	print(type(num))
	print ('你喜爱的数字是%s'%num)
	liuliuliu= 6.66
	print('%s'%num)
	print("自己在下面的空行再打印一句，将liuliuliu的值按四舍五入的方式取整，提示print('%.1f' % num)或print('%d' % (num+0.5)) 或 其它的方式也行，开心就好")

	print(int(round(liuliuliu)))
	print('下面是打开C盘中的C:\Program Files文件夹的一条命令')
	os.startfile(r'C:\Program Files')
	class_object=My_class()
	class_object.printHelloWorld2()
