import random

r = random.randint(1,100)
while True:
	num = int(input('plz guess number: '))
	if num == r:
		print('you are right!')
		break
	elif num > r:
		print('your answer is bigger!')
	elif num < r:
		print('your answer is smaller!')

