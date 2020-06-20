dict_map = {
	'1': 'a',
	'2': 'b',
	'3': 'c',
	'4': 'd',
}

print(dict_map)

for key in dict_map:
	print(key)

for key, value in dict_map.items():
	print(key, value, sep=" - ")

for value in dict_map.values():
	print(value)
