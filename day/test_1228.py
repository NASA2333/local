import os,time

xpaht = r"D:\testclass"
a= os.path.join(xpaht,"lesson.zip")
print(os.path.splitext(a))
# print(a)
# print(os.path.split(a)[1].split('.')[0])
# os.rename(a,os.path.join(xpaht,'0.jpg'))
# c = os.path.getctime(a)
# print(c)
# print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(c)))

# b = [1514463459.7740192,1514473459.7740192,1514483459.7740192,1514413459.7740192,1515463459.7740192,1514463459]
# print(max(b))
# for i in b:
# 	print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(i)))
# print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))
# print(time.localtime())
# import zipfile
# zf = zipfile.ZipFile(a,'r')

# print(len(zf.namelist()))
# print(zf.namelist())

# print(os.getcwd())
print(os.path.split(os.path.abspath(__file__))[1])
print(os.path.dirname(__file__))