"""by Vasily Selivantsev"""
import sys
import math

a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])

x1 = (- b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
x2 = (- b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)

# hard way
# print(math.floor(x1)) if x1 >= 0 else print(math.ceil(x1))
# print(math.floor(x2)) if x2 >= 0 else print(math.ceil(x2))

# easy and obvious way
print(int(x1))
print(int(x2))
