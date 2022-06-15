#dictionary 

words = {
	'ramen' : '拉麵',  #key : value
	'pasta' : '義大利麵'
}

words['tea'] = '茶' #增加新的key和value
print(words)
print(words['ramen'])
print(words['pasta'])


p0 = {
	'name' : 'ramen',
	'price' : '100'
}

p1 = {
	'name' : 'ramen',
	'price' : '50'
}

drinks = [p0, p1]
print(drinks[0]['name'])
print(drinks[1]['price'])