from random import randint

sett = set()
my_dict = {}
i = 0

while True:
	num = randint(1, 10)
	sett.add(num)
	print(num)
	if num not in my_dict:
		my_dict[num] = 0
	my_dict[num] += 1

	i += 1

	if my_dict[num] == 2:
		break

print("set: ", sett)
print("iterations:", i)
print("dict: ", my_dict)
