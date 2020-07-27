def out(*args):  # любое кол-во аргументов
	print(type(args))  # tuple
	for num in args:
		print(num)


out(1, 2, 3)
print()
names = ['a', 'b', 'c']
out(*names)  # или другой тип данных

print()


def printer(**kwargs):
	print(type(kwargs))  # dict
	for key, value in kwargs.items():
		print('{}: {}'.format(key, value))


printer(a=10, b=15, c=20)

my_dict = {
	'x': 25,
	'y': 'some_value',
	'z': {
		'i': 69.420,
		'j': 4 + 5
	}
}

print()
printer(**my_dict)
