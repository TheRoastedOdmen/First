from random import randint as rand
from time import sleep
from statistics import median as med

my_list = []
num_size = rand(5, 20)
for _ in range(num_size):  # we won't use the var in for-cycle so it's _
	my_list.append(rand(0, 100))

my_list.sort()
half_size = len(my_list) // 2
median = None  # we will use it later, that's why None

if num_size % 2 == 1:
	median = my_list[half_size]
else:
	median = sum(my_list[half_size - 1: half_size + 1]) / 2

print("\nrandom list: ", my_list)
print("\ncalculating the median")
sleep(1)
print("\nmedian: ", round(median, 1))
sleep(1)
print("\nmedian through statistics: ", med(my_list))
