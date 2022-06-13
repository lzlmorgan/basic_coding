products = []
while True:
	name = input('please type in the product name: ')
	if name == 'q':
		break
	price = input('please input the current price: ')
	products.append([name, price]) #将list p 放入products清单

for p in products: 
	print(p[0], ' is with the price of', p[1]) #print出list p的第一个0和第二个1


with open('product.csv', 'w') as f:
	for p in products:
		f.write(p[0] + ',' +p[1] + '\n') #string合并 write写入文档 \n回车