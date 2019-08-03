from time import sleep
print('!Module Helper!')

print(help('modules'))

a = str(input('Enter module name: '))

if a == 'math':
    print(help('math'))

elif a == 'time':
    print(help('time'))

elif a == 'random':
    print(help('random'))

else: print('Unknown name')
