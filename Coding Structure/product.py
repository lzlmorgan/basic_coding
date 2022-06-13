products = []
while True:
	name = input('please type in the product name: ')
	if name == 'q':
		break
	price = input('please input the current price: ')
	p = []
	p.append(name)
	p.append(price)
	products.append(p)
print(products)