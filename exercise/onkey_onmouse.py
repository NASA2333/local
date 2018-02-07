import pyHook
import pythoncom,time

def onMouseEvent(event):
	#监听鼠标事件
	print("MessageName:",event.MessageName)							#操作名称
	print("Message:",event.Message)									#事件编号
	print("Time:",event.Time)										#时间
	print("Window:",event.Window)									#视窗编号
	print("WindowName:",event.WindowName)							#视窗名称（路径）
	print("Position:",event.Position)								#坐标
	print("Wheel:",event.Wheel)
	print("Injected:",event.Injected)
	print("----")
	return True
	# 返回 True 以便将事件传给其它处理程序
	# 注意，这儿如果返回 False ，则鼠标事件将被全部拦截

def onKeyboardEvent(event):
	#监听键盘事件
	# print("MessageName:",event.MessageName)								#键盘动作名称
	# print("Message:",event.Message)										#键盘事件编号
	# print("Time:",event.Time)											#时间
	# print("Window:",event.Window)										#视窗编号
	# print("WindowName:",event.WindowName)								#视窗名称\路径
	# print("Ascii:",event.Ascii,chr(event.Ascii))						#ascii转换为键盘显示内容
	# print('key:',event.Key)												#输入内容
	# print("KyeID:",event.KeyID)											#内容编号

	# print("ScanCode:",event.ScanCode)									#扫描码
	# print("Extended:",event.Extended)
	# print("Injected:",event.Injected)
	# print("Alt",event.Alt)
	# print("Transition:",event.Transition)
	# print("----")
	# print(str(event.Key))
	return True
def main():
	#实例化，创建钩子管理对象
	hm = pyHook.HookManager()
	#监听所有键盘事件
	hm.KeyDown = onKeyboardEvent
	#设置键盘钩子
	hm.HookKeyboard()
	# #监听所有鼠标事件
	# hm.MouseAll =onMouseEvent
	# #设置鼠标钩子
	# hm.HookMouse()
	#进入循环。如不手动关闭，程序将一直处于监听状态
	pythoncom.PumpMessages()

if __name__ =="__main__":
	main()




