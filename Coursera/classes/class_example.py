# city.py

"""Класс, который будет принимать на вход название города и будет иметь метод,
который будет возвращать прогноз погоды в этом городе."""

# requests позволит нам работать с http запросами
# dateutil для преобразования строк дат в дату из модуля стандартной библ. datetime

from pprint import pprint  # для красивой печати
from dateutil.parser import parse
import requests


class ApiWeatherForecast:
	"""этот класс будет делать запросы
и мы напишем его так, что, если с API что-нибудь случится, заменить надо будет только его"""
	def __init__(self):  # напишем кеш для множественных обращений
		self._city_cache = {}  #

	def get(self, city):
		if city in self._city_cache:
			return self._city_cache[city]  # будем возвращать данные, которые принадлежат кэшу по городу

		url = f"https://api.weatherbit.io/v2.0/current?city={city},NC&key=e72b9799ee2849db8261ddfc3f6f1c0e"
		pprint("Sending HTTP request")
		data = requests.get(url).json()  # преобразовываем ответ джсона в пайтоновское представление (словарь в данном случае)
		forecast_data = data['data']  # достукиваемся до объекта
		forecast = []  # определим лист словарь
		for day_data in forecast_data:
			forecast.append({
				"datetime": day_data["datetime"],
				"temp": day_data["temp"],
				"city_nameeeeeee": day_data["city_name"]  # "city_name" - ключ в словаре
			})
		self._city_cache[city] = forecast  # обновляем словарь прогнозом погоды, каждый раз, когда приходит запрос

		return forecast


class CityInfo:  # создадим класс
	# переопределяем инициализатор класса - он будет принимать название города и необязательный параметр
	def __init__(self, city, weather_forecast=None):
		self.city = city  # устанавливаем аттрибут экземпляра
		self._weather_forecast = weather_forecast or ApiWeatherForecast
		# приватная переменная к экземпляру класса либо к самому Классу

	def weather_forecast(self):  # этот метод возвращает прогноз погоды
		return self._weather_forecast.get(self.city)  # обратимся к приватному аттрибуту и вызовем у него метод get()


def _main():
	# вынесем экз. на верхний уровень - мы будем его передавать каждый раз, когда создаем экз класса CityInfo
	weather_forecast = ApiWeatherForecast()
	for i in range(5):  # предположим, что пришло 5 запросов
		city_info = CityInfo(input("Enter the name of the city: "), weather_forecast=weather_forecast)  # пишем скелет нашей программы с конца
		pprint(city_info.weather_forecast())  # у инстанции (экземпляра) будет такой метод


"""weather_forecast=weather_forecast - таким образом все экзы CityInfo будут использовать экз ApiWeatherForecast
и, не смотря, что у нас 5 http запросов к Api, Отправится всего один (засчет кеша)"""


if __name__ == "__main__":
	_main()

"""В данном примере мы использовали композицию классов, т.е. внутри класса CityInfo аттрибуту присвоен другой класс"""
"""Мы не обрабатывали исключения"""
