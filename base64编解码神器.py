import base64
import control

while 1:
	print('base64编码解码神器')
	mod = input('1,编码\n2，解码\n请输入1-2：')
	if mod == '1':
		str = input('\n\n请输入要编码的字符串：')
		print('\n\n编码后：'+base64.b64encode(str.encode('utf-8')).decode('utf-8'))
		pass
	elif mod == '2':
		str = input('\n\n请输入要解码的字符串：')
		print('\n\n解码后：'+base64.b64decode(str.encode('utf-8')).decode('utf-8'))
		pass
	else:
		exit()

	control.con()


