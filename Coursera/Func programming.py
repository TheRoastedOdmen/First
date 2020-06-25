def multiply(num):
	def inner(a):
		return a * num  # это - Замыкание: объект num вызывается из области видимости основной функции
	return inner


multiplier_2 = multiply(2)
print(multiplier_2(10))
