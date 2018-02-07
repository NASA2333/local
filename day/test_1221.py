from PIL import Image
# import string
from io import  StringIO

im = Image.open(r'E:\下载内容\getImage.jpg','r')
# im.show()
# print(im.format)   #源格式
# print(im.mode)
#
# x =im.transpose(Image.ROTATE_90)
# x.show()
a = Image.open(StringIO.getvalue(im))

print(a)