import requests
import pprint


def corona_info():
	return requests.get("https://habr.com/ru/company/ruvds/blog/480356/").json()


if __name__ == "__main__":
	pprint.pprint(corona_info())