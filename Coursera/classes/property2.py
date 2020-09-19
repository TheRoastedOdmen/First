"""property так же можно использовать, если нужно модифицировать чтение аттрибута и сделать какую-то работу при чтении:
т.е. не надо менять поведение при изменении/удалении значения"""


class Dog:
	def __init__(self, power):
		self._power = power

	# без следующего метода мы не сможем обратится к power, а только к _power
	@property
	def print_power(self):
		# здесь могут быть полезные вычисления

		return self._power


ben = Dog(5000)
print(ben.print_power)
print(Dog.__class__)
