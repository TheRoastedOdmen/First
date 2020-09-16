class Robot:

	def __init__(self, power):
		self.power = power

	def __str__(self):
		return str(self.power)

	def set_power(self, power):  # рефакторим класс, чтобы отрицательные значение приводили к 0
		if power < 0:
			self.power = 0
		else:
			self.power = power


wall_e = Robot(100)
print(wall_e)
wall_e.power = 200  # установили новое значение
print(wall_e.power)

wall_e.power = -20
print(wall_e.power)

wall_e.set_power(-20)  # вызываем новый метод
print(wall_e.power)  # чтобы не менять код, можно воспользоватся property \/
print()


class Robot2:

	def __init__(self, power):
		self._power = power  # с нижним одинарным подчеркиванием - приватный атрибут

	power = property()  # no need to import it. power is now an object of property
#  3 метода property:

	@power.setter
	def power(self, value):
		if value < 0:
			self._power = 0  # то же самое, что описано в старом классе
		else:
			self._power = value

	@power.getter
	def print_power(self):
		return self._power  # то же самое, что описано в старом классе

	@power.deleter
	def power(self):
		print('make robot useless')
		del self._power


rosa = Robot2(100)
rosa.print_power = -20
print(rosa.print_power)  # не будет нулем, если power будет без подчеркивания

# del rosa.power
# print(rosa.power)  # our str from deleter


