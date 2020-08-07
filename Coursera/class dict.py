class Planet:
	"""This class describes planets"""

	count = 1  # аттрибут класса

	def __init__(self, name, population=None):  # переопределен метод инит
		self.name = name  # аттрибут метода
		self.population = population or []  # аттрибут метода


planet = Planet("Earth")

print(planet.__dict__)

planet.mass = 5.97e24

print(planet.__dict__)
print(Planet.__dict__)
print(planet.__doc__)  # or Planet.__doc__
print(planet.__class__)
