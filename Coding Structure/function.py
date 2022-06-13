#function 函式/功能
#function用来收纳程式代码
#它个功能

def wash(dry=False, water = 8): #定义function def=define def需要设计投币口
	print('add water', water, 'level')
	print('add cleaner')
	print('spin')
	if dry: #if dry is true
		print('dry')
wash()
print('-----------')
wash(water = 10)
print('-----------')
wash(True) #使用function
print('-----------')
wash(False)

print('----------')
def say_hi():
	print('hi')
say_hi()
print('-----------')

def add(x = 0, y = 0): #parameter可以设定预设值 有预设值不用强制设定token
	print(x + y)
add(5) #5默认给x
print('-----------')
add(y = 5) #设置y = 5
print('-----------')
add(3, 4)
print('------------')
add(123, 333)
print('------------')
