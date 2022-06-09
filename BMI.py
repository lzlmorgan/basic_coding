import math

H = float (input('plz type your height: '))
W = float (input('plz type your weight: '))
H = H / 100
BMI = W/H**2
print('your BMI is ', round(BMI))

if BMI < 18.5:
	print('light')
elif BMI >= 18.5 and BMI <24:
	print('normal')
elif BMI >=24 and BMI < 27:
	print('little weighted')
elif BMI >=27 and BMI < 30:
	print('weighted')
elif BMI >=30 and BMI < 35:
	print('overweighted')
else:
	print('too fat.')