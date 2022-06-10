data = []
count = 0
with open ('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 100000 == 0:
			# %求余数整除
			print(len(data))
print('档案读取完成，一共有', len(data),'笔资料')

sum_len = 0
for d in data: 
	sum_len = sum_len + len(d) #初始长度为0，赋值每一笔长度到新的长度，求和
	#print(sum_len)
print('平均长度', sum_len/len(data)) #len(data)

new = []
for d in data: #d是data留言list中每一笔的留言
	if len(d) < 100:
		new.append(d)
print(len(new), '笔留言长度小于100')
print(new[0])
print(new[1])