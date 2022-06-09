pw = 'a123456'
i = 3
while i > 0:
	password = input('plz type in the password: ')
	if pw == password:
		print('you can login')
		break
	else:
		i = i -1
		print('error password', i , ' time left')