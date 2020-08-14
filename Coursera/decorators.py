def stringify(fun):
	return str(fun)


@stringify
def mult(a, b):
	return a * b


print(type(stringify(12)))


def decor(func):
	# return func
	print("this is")


@decor
def decored():
	print("test")


# decored = decor(decored)

# decor(decored)


def decorator(func):
	def new_funk():
		print("goodbye")
	return new_funk


@decorator
def decorated():
	print("hello")


decorated()


