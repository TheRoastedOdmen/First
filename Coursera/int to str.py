int_list = []
for num in range(6):
	int_list.append(num)

str_list = [str(num) for num in range(6)]  # List comprehension (Списочное выражение)

print(str_list)
print(type(str_list[1]))

"""
Easier, using map:


def stringify(int_list):
	return list(map(str, int_list))  # using class str as a function
	

stringify(range(6))
"""

"""Even easier: 
print([str(num) for num in range(6)])"""