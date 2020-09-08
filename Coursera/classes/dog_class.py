from json import dumps


class Pet:  # родительский, базовый, супер класс
	def __init__(self, name):
		self.name = name

	@staticmethod
	def some_effect(expression):
		return '#' + expression + '#'


class Dog(Pet):  # наследует все методы и аттрибуты Pet

	def __init__(self, name, breed=None):
		super().__init__(name)  # вызывали инит из родительского
		self.breed = breed

	def say(self):
		return "{}: waw!".format(self.name)

	def get_breed(self):
		return self.breed


class ExportJSON:

	def to_json(self):
		return dumps({
			"name": self.name,
			"breed": self.breed
		})


class ExDog(Dog, ExportJSON):

	def __init__(self, name, breed=None):
		super().__init__(self.some_effect(name), breed)  # some_effect может быть вызван от любого класса иерархии
		# self.name = Pet.make_bold(name)
		# self.breed = breed
		# эти 2 строчки уже не нужны, т.к. они реализованы в super()

		# вызов super без параметров равносилен передачи в параметры сам класс и селф ( super(ExDog, self) )

	def get_breed(self):
		return "порода: {} - {}".format(self.name, self.breed)


class WoolenDog(Dog, ExportJSON):

	def __init__(self, name, breed=None):
		super(Dog, self).__init__(name)  # если необходимо вызвать метод кокретного класса,
		# то ф-ии супер надо передать родителя
		self.breed = "Шерстяная собака породы {}".format(breed)


dog = Dog("Тарги", "Немец")
print(dog.name, dog.breed, sep=", ")
print(dog.say())

dog = ExDog("Белка", breed="Метис")  # breed= нам нужен только для явного указания
print(dog.to_json())

print(ExDog.__mro__)

dog = WoolenDog("Жучка", "Такса")
print(dog.breed)

dog = ExDog("Фокс", "Мопс")
print(dog.__dict__)
print(dog.get_breed())
