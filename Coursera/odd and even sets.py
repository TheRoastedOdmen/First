odd_set = set()
even_set = set()

for number in range(10):
	if number % 2:
		odd_set.add(number)
	else:
		even_set.add(number)

print("Нечетные: ", odd_set)
print("Четные: ", even_set)

union_set = odd_set | even_set
print("Сложение: ", union_set)  # or: print(odd_set.union(even_set))

intersection_set = union_set & even_set
print("Пересечение: ", intersection_set)
print("Пересечение: ", union_set.intersection(odd_set))

difference_set = union_set - even_set
print("Разница: ", difference_set)
print("Разница: ", union_set.difference(odd_set))

symmetric_difference_set = even_set^odd_set
print("Симметрическая разница: ", symmetric_difference_set)
print("Симметрическая разница: ", odd_set.symmetric_difference(even_set))

print(union_set.pop())
