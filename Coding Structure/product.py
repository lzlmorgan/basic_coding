products = []
while True:
	name = input('please type in the product name: ')
	if name == 'q':
		break
	price = input('please input the current price: ')
	p = [] #生成一个小list去包涵name和price
	p.append(name)
	p.append(price)
	products.append(p) #将list p 放入products清单
print(products)

print(products[0][0]) #在清单中拿出其一个list的第一个值