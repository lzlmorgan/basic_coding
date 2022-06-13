products = []
while True:
	name = input('please type in the product name: ')
	if name == 'q':
		break
	price = input('please input the current price: ')
	products.append([name, price]) #将list p 放入products清单
print(products)
