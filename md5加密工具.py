import hashlib
import control

while 1:

	str = input('\n\n输入要加密的数据：')
	print('\n\nmd5加密后的数据为：' + hashlib.md5(str.encode('utf-8')).hexdigest())


	control.con()

