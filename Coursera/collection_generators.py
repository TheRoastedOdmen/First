square_list = [number ** 2 for number in range(10) if number % 2 == 0]
square_dict = {num: num ** 2 for num in range(10)}
square_set = (num for num in range(10))  # generator object
# правильно:
right_set = {num for num in range(10)}

print(square_list)
print(square_dict)
print(square_set)
print(right_set)

gen_object = (x ** 2 for x in range(5))
print(gen_object)  # generator object по которому можно итерироваться:
for i in gen_object:
	print(i)
