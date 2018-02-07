import os,time,zipfile,sys,re

# determine if application is a script file or frozen exe
if hasattr(sys, "frozen"):
	application_path = os.path.dirname(sys.executable)
	xpath =application_path
else:
	xpath = os.path.dirname(__file__)

class DecideMprx():
	def select_file(self):
		'''获取mprx'''
		file_list = []
		for topfile,secondfile,file in os.walk(xpath):
			for i in file:
				file_list.append(os.path.join(topfile,i))
		file_list =[i for i in file_list if os.path.splitext(i)[1] =='.mprx']
		return file_list


	def rename(self):
		'''重命名'''
		name = self.select_file()
		for i in name:
			namelist = os.path.split(i)
			name_2 = namelist[1].split('.')
			newname = os.path.join(namelist[0],(name_2[0]+'.zip'))
			os.rename(i,newname)
			self.decidezip(newname)
			os.rename(newname,i)

	def decidezip(self,name):
		zf = zipfile.ZipFile(name,'r')
		filelong = zf.namelist()
		filestr = ''.join(filelong)
		if re.findall(r"MPRX/MultiMedia",filestr):
			pass
			# print("导出文件:",os.path.split(name)[1])
			# print("\033[1;30;42m文件内容正常\033[0m")
			# print("文件%s 内容正常"%os.path.split(name)[1].split('.')[0])
		else:
			# print("导出文件:",os.path.split(name)[1])
			# print("\033[1;30;41m数据媒体文件丢失\033[5m")
			print("文件 %s \tMultiMedia文件夹丢失"%os.path.split(name)[1].split('.')[0])

if __name__ =="__main__":
		start = DecideMprx()
		start.rename()
		time.sleep(500000)


