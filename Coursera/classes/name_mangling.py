class Pet:  # родительский, базовый, супер класс
	def __init__(self, name):
		self.name = name


class Dog(Pet):

	def __init__(self, name, breed=None):
		super().__init__(name)
		self.__breed = breed  # делаем аттрибут приватным - он будет недоступен для наследников

	def say(self):
		return "{}: AI".format(self.name)

	def get_breed(self):
		return self.__breed


class ExDog(Dog):
	# def __init__(self, name, breed=None):
	# 	super().__init__(name, breed)

	def get_breed(self):
		return "порода: {} - {}".format(self.name, self.__breed)  # нам нужно _Dog__breed, чтоб можно было вызвать ф-ию


dog = ExDog("Фокс", "Мопс")
print(dog.__dict__)  # покажет аттрибуты
# print(dog.get_breed())
