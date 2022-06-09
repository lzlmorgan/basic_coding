import random

start = int(input('plz decide your start number!  '))
end = int(input('plz decide your end number!  '))

r = random.randint(start, end)
count = 0
while True:
	count += 1
	num = int(input('plz guess number: '))
	if num == r:
		print('you are right!')
		print('this is the', count, 'time for you')
		break
	elif num > r:
		print('your answer is bigger!')
	elif num < r:
		print('your answer is smaller!')
	print('this is the', count, 'time for you')

