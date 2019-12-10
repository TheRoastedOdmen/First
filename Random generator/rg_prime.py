from random import randint
from time import sleep

amount = int(input("Quantity of numbers: "))
range_start = int(input("From: "))
range_end = int(input("To: "))

generated_list = []

def is_prime_number(x):
    divisor = 2
    while divisor < x:
        if x % divisor == 0:
            return False
        divisor += 1
    return True

print('Let the generation commence ^ , ^')

sleep(1)

while amount > 0:
    random_i = randint(range_start, range_end)
    if is_prime_number(random_i):
        generated_list.append(random_i)
        amount -= 1

print('Result:',generated_list)