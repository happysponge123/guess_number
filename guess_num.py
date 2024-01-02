import random

r = random.randint(1, 100)

while True:
	num = int(input('猜數字'))
	if num == r:
		print('猜對了!')
		break
	elif num > r:
		print('比答案大')
	else : #num < r
		print('比答案小')
