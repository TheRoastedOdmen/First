def first_decorator(func):
	def wrapped():
		return '1 ' + func() + ' 1'
	return wrapped


def second_decorator(func):
	def wrapped():
		return '2 ' + func() + ' 2'
	return wrapped


@first_decorator
@second_decorator  # firstly this
def func():
	return "whoah"


print(func())
