data = []
with open ('food.txt', 'r') as f:
	#as当作f档案
	for line in f:
		#print(line)
		data.append(line.strip()) #把每一个line放入data清单list
		#.strip()去掉换行符\n

	print(data)