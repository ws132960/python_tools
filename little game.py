# a=1
# while a<=100:
# 	if a%7==0 or a%10==7 or a//10==7:
# 		a+=1
# 		continue
# 		pass
# 	print(a)
# 	a+=1
# 	pass
# print('jo\nvi')
# input()
import random
a = random.randint(0,9)
sum = 1
while sum <= 3:
	print('****'*10)
	flag = input('请输入：')
	if int(flag) == a:
		print('猜对了,答案是{}'.format(a))
		break
	else :
		print('猜错了，提示：',end = '')
		if int(flag) > a:
			print('大了')
		else :
			print('小了')
			pass
		pass
	if sum == 3:
		print('****'*10)
		print('全猜错了,答案是{}'.format(a))
	sum += 1
	pass
input()