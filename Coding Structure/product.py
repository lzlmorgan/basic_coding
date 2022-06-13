#读取档案
products = []
with open('products.csv', 'r', encoding = 'utf-8') as f:
	for line in f:
		name, price = line.strip().split(',') #strip()去掉\n尾部回车 & split分割数据by comma s是清单
		products.append([name, price])
print(products)


while True:
	name = input('please type in the product name: ')
	if name == 'q':
		break
	price = input('please input the current price: ')
	price = int(price) #转换price到integer
	products.append([name, price]) #将list p 放入products清单

for p in products:
	print(p[0], ' is with the price of', p[1]) #print出list p的第一个0和第二个1


with open('products.csv', 'w', encoding = 'utf-8') as f: #encoding加入编码规则
	f.write('product, price\n') #加入column的名字product和price
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n') #string合并 write写入文档 \n回车
