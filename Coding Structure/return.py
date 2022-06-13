#return 回传
#function如果有return，就可以把function执行的结果存下来
#可以想象function运行后会把【化身】成为return的东西

def add(x, y):
	return x + y
result = add(3, 4)
print(result)



def average(numbers):
	return sum(numbers) / len(numbers) #除法自动转化为float	
print(average([1, 2, 3]))
print(average([21,333,200]))

