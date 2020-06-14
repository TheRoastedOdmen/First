"""by Vasily Selivantsev"""

import sys

digit_string = sys.argv[1]
num = int(digit_string)

summary = 0
while num > 0:
	summary += num % 10
	num //= 10

print(summary)

"""Компактное решение:
import sys
print(sum([int(x) for x in sys.argv[1]]))
"""