class Human:

	def __init__(self, name, age=0):
		self.name = name
		self.age = age

	@staticmethod  # decorator, no need to import it
	def is_age_valid(age):  # можно было реализовать с пом. обычной функции вне пространства имен класса
		return 0 < age < 150


print(Human.is_age_valid(35))  # from class

human = Human("Old Bob")
print(human.is_age_valid(234))  # from instance of class
