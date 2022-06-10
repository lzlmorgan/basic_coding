data = []
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)


# good = []
# for d in data:
# 	if 'good' in d:
# 		good.append(d)
good =[d for d in data if 'good' in d]
print(len(good)) 

good = [1 for d in data if 'good' in d] #把1装入清单，当遇见一笔有good的留言
print(good)

bad = ["bad" in d for d in data] #留言中有bad就显示true
print(bad)