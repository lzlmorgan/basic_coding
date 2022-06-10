data = []
count = 0
with open ('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:
			# %求余数整除
			print(len(data))
print('档案读取完成，一共有', len(data),'笔资料')