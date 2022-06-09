pw = 'a123456'
i = 3
while True:
	password = input('plz type in the password: ')
	if pw == password:
		print('you can login')
		break
	else:
		i = i -1
		print('error password', i , ' time left')
		if i == 0:
			break
