import random
r = random.randint(1, 100)
while true:
	num = input('請猜數字: ')
	num = int(num)
	if num > r:
		print('太大! 在小一點')
	elif num < r:
		print('太小! 在大一點')
	else:
		print('終於猜對了!')
		break