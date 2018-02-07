##获取图片尺寸  600*840
from PIL import Image
import os


# filename =r'D:\baidu_image\NBA\1.jpg'
#
# a = Image.open(filename)
# print(a.size)
# print(max(a.size))
# out = a.resize((600,480))
# b = a.resize((500,500),Image.ANTIALIAS)						#修改图片大小
# b.save(r'D:\baidu_image\NBA\0.1.jpg',quality =100)
# path = r"D:\baidu_image\NBA"
# for i,j,x in os.walk(path):
# 	# print(i)
# 	for z in x:
# 	# 	print(z)
# 		print(os.path.join(i,z))


class ChangeImageSize():
	def __init__(self):
		self.path_list =[]

	def get_path(self,path):
		for firstpath,second,filename in os.walk(path):
			for i in filename:
				self.path_list.append(os.path.join(firstpath,i))
		return self.path_list

	def changesize(self):
		imagedel_list=[]
		for i in self.path_list:
			# print(i)
			img = Image.open(i).convert('RGB')
			if min(img.size)<300:
				pass

			elif img.size[0]<800 or img.size[1] <840:
				print(i+'\t',img.size)
				imagedel_list.append(i)
				newimg = img.resize((800,840))
				# newpath=os.path.join(os.path.split(i)[0],'%s.jpg'%(os.path.split(i)[1].split(".")[0]+'_1'))   #当前文件夹
				newpath=os.path.join(r'd:\tt','%s.jpg'%(os.path.split(i)[1].split(".")[0]+'_1'))
				# print(newpath)
				newimg.save(newpath,quality =100)

		return imagedel_list

	def imgdel(self):
		a =self.changesize()
		for i in a:
			os.remove(i)

if __name__=="__main__":
	xpath = r"D:\baidu_image\bookimage"
	a = ChangeImageSize()
	a.get_path(xpath)
	a.imgdel()
	# print(os.path.split(xpath)[1].split(".")[0]+'_1'+'.jpg')
	# print(os.path.join(os.path.split(xpath)[0],(os.path.split(xpath)[1].split(".")[0]+'-1'+'.jpg')))