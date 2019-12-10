from random import randint
from time import sleep

amount = int(input("Quantity of numbers: "))
range1 = int(input("From: "))
range2 = int(input("To: "))

generated_list = []

print('Let the generation commence ^ . ^')

sleep(1)

while amount > 0:
    random_i = randint(range1, range2)
    generated_list.append(random_i)
    amount -= 1

print('Result:',generated_list)