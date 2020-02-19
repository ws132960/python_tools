import requests
import control

while 1:
	url = input('\n\n请输入url：')
	response = requests.get(url)

	print('\n\n响应内容：\n\n')
	print('包头：\n\n')
	for i in response.headers:
		print(i + ' : ' + response.headers[i])
	print('\n\n源码：\n\n' + response.text)


	control.con()