products = []

while True:
	name = input('please type in the product name: ')
	if name == 'q':
		break
	
	products.append(name)
	print(products)