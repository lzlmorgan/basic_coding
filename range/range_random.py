import random

for i in range(3):  #完成三次loop
	r = random.randint(1,100) #从1-100找到三个随机数
	print('this is the ', i + 1, 'time to print random number--', r)

print('-------')
for n in range(3):
	r = random.randint(1,100)
	print(r)