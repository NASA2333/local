import os,time,zipfile,sys,re

# determine if application is a script file or frozen exe
if hasattr(sys, "frozen"):
	application_path = os.path.dirname(sys.executable)
	xpath =application_path
else:
	xpath = os.path.dirname(__file__)

class DecideMprx():
	Newname =''
	def select_file(self):
		'''获取创建时间最近的文件mprx'''
		# print("当前地址：",xpath)
		self.file_list = []
		times =[0]
		name =''
		for topfile,secondfile,file in os.walk(xpath):
			for i in file:
				self.file_list.append(os.path.join(topfile,i))
		for i in self.file_list:
			if os.path.splitext(i)[1] =='.mprx':			#文件后缀
				time1 =os.path.getctime(i)
				if time1 >times[0]:
					times[0]=time1
					name = i

		# print("最新的文件是:%s,创建时间是%s"%(name,times[0]))
		return name


	def rename(self):
		'''重命名'''
		name = self.select_file()
		if name !=self.Newname:
			namelist = os.path.split(name)
			name_2 = namelist[1].split('.')
			newname = os.path.join(namelist[0],(name_2[0]+'.zip'))
			os.rename(name,newname)
			self.decidezip(newname)
			os.rename(newname,name)
			self.Newname=name
		else:
			# print("文件未更新")
			# print(".")
			pass

	def decidezip(self,name):

		zf = zipfile.ZipFile(name,'r')
		filelong = zf.namelist()
		filestr = ''.join(filelong)
		if re.findall(r"MPRX/MultiMedia",filestr):
			# print("导出文件:",os.path.split(name)[1])
			# print("\033[1;30;42m文件内容正常\033[0m")
			print("文件%s 内容正常"%os.path.split(name)[1].split('.')[0])
		else:
			# print("导出文件:",os.path.split(name)[1])
			# print("\033[1;30;41m数据媒体文件丢失\033[5m")
			print("文件 %s MultiMedia文件夹丢失"%os.path.split(name)[1].split('.')[0])

if __name__ =="__main__":
	start = DecideMprx()
	while 1:
		start.rename()
		start.rename()
		time.sleep(15)
