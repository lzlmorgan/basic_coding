pw = 'a123456'
i = 3
while i > 0:
	i = i - 1
	password = input('plz type in the password: ')
	if pw == password:
		print('you can login')
		break
	else:
		if i > 0:
			print('password error! ', 'You have ', i , ' times left')
		else:
			print('you do not have any chance to try')