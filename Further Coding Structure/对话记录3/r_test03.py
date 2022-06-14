lines = []
with open('3.txt', 'r', encoding = 'utf-8-sig') as f:
	for line in f:
		lines.append(line)
	
for line in lines:
	s = line.split()
	time = s[0][:5] #先取s清單的每一個的第一個元素，在去第一個元素從第五個字符之手的內容
	name = s[0][5:]
	print(name)
	print(time)