#默认情况下使用
# import qrcode
'''
img =qrcode.make("内容")
img.save("path and name")
'''


#更多设置
'''
img = qrcode.QRCode(
	version=1,						#1-40个版本，指二维码长宽对应平分多少分，1对应的是21*21，每增加一个版本，增加4个尺寸，
	error_correction=qrcode.ERROR_CORRECT_L,		#容错等级，分为L\M\Q\H,分别对应7%\15%(默认）\25%\30%
	box_size=20,					#生成图片的像素
	border=4,						#二维码边框宽度，4为最小值
)
img.add_data("数据内容")
img.make(fit=True)

iamge = img.make_image()
iamge.save("path and name")
'''

import qrcode,os,time
class MakeQrcode():
	def __init__(self):
		self.data = input("请输入你想要转换的内容：")

	def make_qrcode(self):
		path1 = r"D:\baidu_image\QRcode"
		if not os.path.exists(path1):
			os.makedirs(path1)
		T= int(time.time())
		img = qrcode.make(self.data)
		img.save(os.path.join(path1,str(T)+".png"))

MakeQrcode().make_qrcode()