class Rectangle:
	def __init__(self, width, height):
		self.width = width
		self.height = height

	def area(self):
		return self.width * self.height


a = Rectangle(10, 20)
print(a.area())  # 200

Rectangle.__init__(a, 2, 5)  # так можно переопределить конструктор экзмепляра, первый аргумент - наш self
b = a.area()  # 10
print(b)  # b - class 'int'


class Rectangle2:  # а второму классу инициализатор не будем переопределять
	# тогда метод нужно определить следующим образом:
	def area(this, width, height):  # self можно переименовывать (но не нужно)
		return width * height


c = Rectangle2()
# вот как питон понимает вызов метода area, с - self(this)
print(Rectangle2.area(c, 2, 4))  # 8
