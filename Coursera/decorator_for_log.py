from functools import wraps as wraps


def logger(filename):
	def decorator(func):
		@wraps(func)  # name of the func will be multiply_list
		def wrapped(num_list):  # *args, **kwargs for unlimited arguments
			res = func(num_list)
			with open('new_log.txt', 'w') as l:  # 4. Запись результатов в файл
				l.write(str(res))
			return res  # Возврат основной функции, а точнее - ее результата
		return wrapped  # 3. Декоратор возвращает новую функцию wrapped, которая подменяет multiply_list
	return decorator  # 2. Возвращается декоратор - он принимает ф-ию (в данном случае multiply_list)


# без синтаксического сахара multiply_list = logger('new_log.txt')(multiply_list)
@logger("new_log.txt")  # 1. Вызывается ф-ия logger, которой мы передаем filename
def multiply_list(num_list):
	j = 1
	for i in num_list:
		j *= i
	return j


print("multor: {}".format(multiply_list([1, 2, 3, 4, 5])))
print("name of the function: {}".format(multiply_list.__name__))

with open('new_log.txt', 'r') as f:
	print('log: {}'.format(f.read()))
