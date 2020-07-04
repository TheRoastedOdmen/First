"""by Vasily Selivantsev"""

import sys

digit_string = sys.argv[1]
step = int(digit_string)

a = "#"
b = " "
for i in range(1, step + 1):
	print(b * (step - i) + a * i)
