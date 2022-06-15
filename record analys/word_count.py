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

wc = {} #word count
for d in data:
	words = d.strip().split() #split预设值直接去掉空白
	for word in words:
		if word in wc:
			wc[word] += 1 #已知key+1
		else:
			wc[word] = 1 #新增key进字典

for word in wc:
	if wc[word] > 1000000:
		print(word, wc[word])

while True:
	word = input('plz type the word: ')
	if word == 'q':
		break
	if word in wc:
		print('your key word shows', wc[word], 'times')
	else:
		print('No such word in reviews')