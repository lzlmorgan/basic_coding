products = []
while True:
	name = input('please type in the product name: ')
	if name == 'q':
		break
	price = input('please input the current price: ')
	products.append([name, price]) #将list p 放入products清单
print(products)

for p in products: 
	print(p) #print出products list中每一个小list p
	print(p[0], ' is with the price of', p[1]) #print出list p的第一个0和第二个1
