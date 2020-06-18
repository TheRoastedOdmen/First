from random import randint

my_set = set()  # используем множество, из-за ее особенности хранить только уникальные значения
checker = 0  # с этой переменной будем сравнивать длину my_set
iterations = 0  # счетчик итераций

while True:
	num = randint(1, 10)
	print(num)  # для проверки, а так отдельно переменную num можно не вводить
	my_set.add(num)
	iterations += 1

	if len(my_set) > checker:
		checker += 1
	else:
		break  # выходим из цикла как только длина my_set прировняется чекеру

print("set: ", my_set)  # тоже для проверки
print("number of iterations: ", iterations)

# easier and for other mutable collections

print("\n")
my_set = list()

while True:
	num = randint(1, 10)
	print(num)
	if num in my_set:
		break
	my_set.append(num)

print(my_set)
print(len(my_set) + 1)
