from datetime import date


def extract_description(user_string):  # функция-заглушка для примера
	return "открытие чемпионата мира по футболу"


def extract_date(user_string):  # функция-заглушка для примера
	return date(2018, 6, 14)


class Event:

	def __init__(self, description, event_date):
		self.date = event_date
		self.description = description

	def __str__(self):
		return f"Event \"{self.description}\" at {self.date}"

	@classmethod  # decorator, no need to import it
	def from_string(cls, user_input):  					# в отличие от метода экземпляра, классметод принимает не ссылку
		description = extract_description(user_input)  # на конкретный экземпляр (селф), а сам класс непосредственно (Event)
		date = extract_date(user_input)
		return cls(description, date)  # проинициализируем класс и вернем его экземпляр на основе инпута
# без классметода мы не сможем вернуть экземпляр, т.е. ^ не будет работать
# from_string не сможет обратится к user_input


event_description = "Рассказать, что такое @classmethod"
event_date = date.today()

event = Event(event_description, event_date)  # создаем экземпляр класса Event, инициализируя его через аттрибуты
print(event)

event = Event.from_string("Добавить в мой календарь открытие чемпионата мира по футболу на 14 июня 2018 года")
# мы использовали метод класса, который принимает строку, анализирует ее и возвращает на экземпляр класса Event - event
print(event)
print()
print(dict.fromkeys("12345"))  # тоже применение классметода
# fromkeys - метод класса, принимает итерабельный объект и возвращает проинициализированный словарь
