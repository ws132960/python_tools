import requests
import control
while 1:

	url = input('请输入url：')
	mod = input('需要发送? 1,get包 2,post包 ：')
	num = int(input('需要上传的变量数：'))
	data = {}
	i = 0
	while num > i:
		key = input('第{}个需要上传的变量名：'.format(i+1))
		value = input(key + '的值：')
		data.update({key : value})
		i += 1

	if mod == '1':
		response = requests.get(url,params = data)
	elif mod == '2':
		response = requests.post(url,data = data)
	else :
		exit()

	print('\n\n响应内容：\n\n')
	print('包头：\n\n')
	for i in response.headers:
		print(i + ' : ' + response.headers[i])
	print('\n\n源码：\n\n' + response.text)

	control.con()

