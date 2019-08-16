from time import sleep
from math import factorial
#import numpy

u = '\nL I S T   C A L C U L A T O R\n'
print('#' * ((len(str(u))) - 2))
print(u)
print('#' * ((len(str(u))) - 2))

print('\nFirstly choose an option\n'
    'Then input the numbers via enter\n'
    'When you done inputting press enter to get the result\n'
    'Note that yopu can input any amount of numbers\n')

f = open('calculator_log.txt', 'w')
f.write('\n')

while True:
    try:
        print("\n__________OPTIONS___________ \n"
            "\nInput '+' to add the numbers\n"
            "Input '-' to substract the numbers\n"
            "Input '*' or 'x' to multiply the numbers\n"
            "Input '/' to divide the numbers\n"
            "Input '**' or '^' to exponentiation of the numbers\n"
            "Input 'y/x' to divide 1 number to a list of numbers (also %)\n"
            "Input 'x/y' to divide a list of number to a 1 number (also %)\n"
            "Input '!' to factorial the numbers\n"
            "Input 'openlast' to see the last result\n"
            "Input 'openlog' to see the log of the session\n"
            "\nInput 'exit' to quit the program")

        f = open('Calculator_log.txt', 'a')
        a = str(input("\nChoose an option: "))
        n = 1
        y = []
        #np.seterr(divide='ignore')

        if a == "exit":
            break
        

#Addition module

        elif a == '+':
            print('\nYou have choosen the Addition\n')
            x = float(input('Enter the number: '))
            print(str(n) + 'st number:-->',x)

            while True:
                try:
                    n += 1
                    y.append(x)
                    x = float(input('Enter the number: '))
                    if len(y)%10 == 0 and len(y) != 10:
                        print(str(n) + 'st number:-->',x)
                    elif len(y)%10 == 1 and len(y) != 11:
                        print(str(n) + 'nd number:-->',x)
                    elif len(y)%10 == 2 and len(y) != 12:
                        print(str(n) + 'rd number:-->',x)
                    elif len(y) > 2:
                        print(str(n) + 'th number:-->',x)
                except:
                    break

            u1 = 'Addition result: '
            print()
            print('+' * (len(u1) + len(str(sum(y))) + 1), '\n')
            print(u1, sum(y), '\n')
            print('+' * (len(u1) + len(str(sum(y))) + 1))

            file = open('last_calculator_result.txt', "w")
            file.write('+')
            file.write('\n\nLast ')
            file.write(str(u1))
            file.write(str(sum(y)))
            file.write('\n\n+')
            file.close()

            f.write('\n')
            f.write(str(u1))
            f.write(str(sum(y)))
            f.write('\n')

            sleep(1)


#Substraction module

        elif a == '-':
            print('\nYou have choosen the Substraction\n')
            x = float(input('Enter the number: '))
            print(str(n) + 'st number:-->',x)

            while True:
                try:
                    n += 1
                    y.append(x)
                    x = float(input('Enter the number: '))*-1
                    if len(y)%10 == 0 and len(y) != 10:
                        print(str(n) + 'st number:-->',x*-1)
                    elif len(y)%10 == 1 and len(y) != 11:
                        print(str(n) + 'nd number:-->',x*-1)
                    elif len(y)%10 == 2 and len(y) != 12:
                        print(str(n) + 'rd number:-->',x*-1)
                    elif len(y) > 2:
                        print(str(n) + 'th number:-->',x*-1)
                except:
                    break

            u1 = 'Substraction result: '
            print()
            print('-' * (len(u1) + len(str(sum(y))) + 1), '\n')
            print(u1, sum(y), '\n')
            print('-' * (len(u1) + len(str(sum(y))) + 1))

            file = open('last_calculator_result.txt', "w")
            file.write('-')
            file.write('\n\nLast ')
            file.write(str(u1))
            file.write(str(sum(y)))
            file.write('\n\n-')
            file.close()

            f.write('\n')
            f.write(str(u1))
            f.write(str(sum(y)))
            f.write('\n')


            sleep(1)


#Multiplication module

        elif a == '*' or a == 'x':
            print('\nYou have choosen the Multiplication\n')
            x = float(input('Enter the number: '))
            print(str(n) + 'st number:-->',x)

            while True:
                try:
                    n += 1
                    y.append(x)
                    x = float(input('Enter the number: '))
                    if len(y)%10 == 0 and len(y) != 10:
                        print(str(n) + 'st number:-->',x)
                    elif len(y)%10 == 1 and len(y) != 11:
                        print(str(n) + 'nd number:-->',x)
                    elif len(y)%10 == 2 and len(y) != 12:
                        print(str(n) + 'rd number:-->',x)
                    elif len(y) > 2:
                        print(str(n) + 'th number:-->',x)
                except:
                    break

            def multi(y):
                res = 1
                for x in y:
                    res = res * x
                return res

            u1 = 'Multiplication result: '
            print()
            print('x' * (len(u1) + len(str(multi(y))) + 1), '\n')
            print(u1, multi(y), '\n')
            print('x' * (len(u1) + len(str(multi(y))) + 1))

            file = open('last_calculator_result.txt', "w")
            file.write('x')
            file.write('\n\nLast ')
            file.write(str(u1))
            file.write(str(multi(y)))
            file.write('\n\nx')
            file.close()

            f.write('\n')
            f.write(str(u1))
            f.write(str(multi(y)))
            f.write('\n')

            sleep(1)


#Division module

        elif a == '/':
            print('\nYou have choosen the Division\n')
            x = float(input('Enter the number: '))
            print(str(n) + 'st number:-->',x)

            while True:
                try:
                    n += 1
                    y.append(x)
                    x = 1/float(input('Enter the number: '))
                    if len(y)%10 == 0 and len(y) != 10:
                        print(str(n) + 'st number:-->',1/x)
                    elif len(y)%10 == 1 and len(y) != 11:
                        print(str(n) + 'nd number:-->',1/x)
                    elif len(y)%10 == 2 and len(y) != 12:
                        print(str(n) + 'rd number:-->',1/x)
                    elif len(y) > 2:
                        print(str(n) + 'th number:-->',1/x)

                    # TODO: Program has to delete x = 0 value and continue
                    #       to append(x) (same to y/x and x/y)
                except:
                    break

            def div(y):
                res = 1
                for x in y:
                    res = res * x
                return res

            u1 = 'Division result: '
            print()
            print('/' * (len(u1) + len(str(div(y))) + 1), '\n')
            print(u1, div(y), '\n')
            print('/' * (len(u1) + len(str(div(y))) + 1))

            file = open('last_calculator_result.txt', "w")
            file.write('/')
            file.write('\n\nLast ')
            file.write(str(u1))
            file.write(str(div(y)))
            file.write('\n\n/')
            file.close()

            f.write('\n')
            f.write(str(u1))
            f.write(str(div(y)))
            f.write('\n')

            sleep(1)


#List calculator modules

#Exponentiation module

        elif a == '**' or a == '^':
            print('\nYou have choosen the Exponentiation\n')
            x = float(input('Enter the number: '))
            print(str(n) + 'st number:-->',x)

            while True:
                try:
                    n += 1
                    y.append(x)
                    x = float(input('Enter the number: '))
                    if len(y)%10 == 0 and len(y) != 10:
                        print(str(n) + 'st number:-->',x)
                    elif len(y)%10 == 1 and len(y) != 11:
                        print(str(n) + 'nd number:-->',x)
                    elif len(y)%10 == 2 and len(y) != 12:
                        print(str(n) + 'rd number:-->',x)
                    elif len(y) > 2:
                        print(str(n) + 'th number:-->',x)
                except:
                    break

            v = float(input('Enter the exponent: '))
            print('\nExponent:--->', v)

            def m(x):
                y2 = 0 
                for x in y:
                    y2 = x**v
                    yield y2

            maxy2 = [x**v for x in y]
            
            u1 = 'Exponentiation result: '
            print()
            print('^' * (len(u1) + len(str(max(maxy2))) + 1), '\n')
            for y2 in m(x):
                print(u1, y2, '\n')
            print('^' * (len(u1) + len(str(max(maxy2))) + 1))

            file = open('last_calculator_result.txt', "w")
            file.write('^')
            file.write('\n\nLast ')
            file.write(str(u1))
            file.write('\n')
            for y2 in m(x):
                file.write(str(y2))
                file.write('\n')
            file.write('\n^')
            file.close()

            f.write('\n')
            f.write(str(u1))
            f.write('\n')
            for y2 in m(x):
                f.write(str(y2))
                f.write('\n')
            f.write('\n')

            sleep(1)


#y/x module

        elif a == 'y/x':
            print('\nYou have choosen the y/x\n')
            z = float(input('Enter the main number (y): '))
            print('Main number (y): ', z)
            x = float(input('Enter the number (x): '))
            print(str(n) + 'st number (x): ',x)

            while True:
                try:
                    n += 1
                    y.append(x)
                    x = float(input('Enter the number (x): '))
                    if len(y)%10 == 0 and len(y) != 10:
                        print(str(n) + 'st number (x): ',x)
                    elif len(y)%10 == 1 and len(y) != 11:
                        print(str(n) + 'nd number (x): ',x)
                    elif len(y)%10 == 2 and len(y) != 12:
                        print(str(n) + 'rd number (x): ',x)
                    elif len(y) > 2:
                        print(str(n) + 'th number (x): ',x)
                except:
                    break

            def m(x):
                y2 = 0 
                for x in y:
                    y2 = x**v
                    yield y2

            maxy2 = [x**v for x in y]
            
            u1 = 'y/x result: '
            print()
            print('/' * (len(u1) + len(str(y2)) + 1), '\n')
            print(u1, y2, '\n')
            print('/' * (len(u1) + len(str(y2)) + 1))

            file = open('last_calculator_result.txt', "w")
            file.write('//')
            file.write('\n\nLast ')
            file.write(str(u1))
            file.write('\n')
            for y2 in m(x):
                file.write(str(y2))
                file.write('\n')
            file.write('\n//')

            f.write('\n')
            f.write(str(u1))
            for y2 in m(x):
                f.write(str(y2))
                f.write('\n')
            f.write('\n')

            y3 = [(str(res*100) + '%') for res in y2]

            u2 ='y/x % result: '
            print()
            print('%' * (len(u2) + len(str(y3)) +1), '\n')
            print(u2, y3, '\n')
            print('%' * (len(u2) + len(str(y3)) +1))

            file.write('\n\n\n%')
            file.write('\n\nLast ')
            file.write(str(u2))
            file.write(str(y3))
            file.write('\n\n%')
            file.close()

            f.write('\n')
            f.write(str(u2))
            f.write(str(y3))
            f.write('\n')

            sleep(1)


#x/y module

        elif a == 'x/y':
            print('\nYou have choosen the x/y\n')
            x = float(input('Enter the number (x): '))
            print(str(n) + 'st number (x): ',x)

            while True:
                try:
                    n += 1
                    y.append(x)
                    x = float(input('Enter the number (x): '))
                    if len(y)%10 == 0 and len(y) != 10:
                        print(str(n) + 'st number (x): ',x)
                    elif len(y)%10 == 1 and len(y) != 11:
                        print(str(n) + 'nd number (x): ',x)
                    elif len(y)%10 == 2 and len(y) != 12:
                        print(str(n) + 'rd number (x): ',x)
                    elif len(y) > 2:
                        print(str(n) + 'th number (x): ',x)
                except:
                    break

            z1 = float(input('Enter the division number (y): '))
            print('Division number (y): ', z1)

            y2 = [x/z1 for x in y]
            
            u1 = 'x/y result: '
            print()
            print('/' * (len(u1) + len(str(y2)) + 1), '\n')
            print(u1, y2, '\n')
            print('/' * (len(u1) + len(str(y2)) + 1))

            file = open('last_calculator_result.txt', "w")
            file.write('//')
            file.write('\n\nLast ')
            file.write(str(u1))
            file.write(str(y2))
            file.write('\n\n//')

            f.write('\n')
            f.write(str(u1))
            f.write(str(y2))
            f.write('\n')

            y3 = [(str(res*100) + '%') for res in y2]

            u2 ='x/y % result: '
            print()
            print('%' * (len(u2) + len(str(y3)) +1), '\n')
            print(u2, y3, '\n')
            print('%' * (len(u2) + len(str(y3)) +1))

            file.write('\n\n\n%')
            file.write('\n\nLast ')
            file.write(str(u2))
            file.write(str(y3))
            file.write('\n\n%')
            file.close()

            f.write('\n')
            f.write(str(u2))
            f.write(str(y3))
            f.write('\n')

            sleep(1)


#Factorial module

        elif a == '!':
            print('\nYou have choosen the Factorial\n')
            x = int(input('Enter the number: '))
            print(str(n) + 'st number:-->',x)

            while True:
                try:
                    n += 1
                    y.append(x)
                    x = int(input('Enter the number: '))
                    if len(y)%10 == 0 and len(y) != 10:
                        print(str(n) + 'st number:-->',x)
                    elif len(y)%10 == 1 and len(y) != 11:
                        print(str(n) + 'nd number:-->',x)
                    elif len(y)%10 == 2 and len(y) != 12:
                        print(str(n) + 'rd number:-->',x)
                    elif len(y) > 2:
                        print(str(n) + 'th number:-->',x)
                except:
                    break

            y2 = [factorial(x) for x in y]

            u1 = 'Factorial result: '
            print()
            print('!' * (len(u1) + len(str(y2)) + 1), '\n')
            print(u1, y2, '\n')
            print('!' * (len(u1) + len(str(y2)) + 1))

            file = open('last_calculator_result.txt', "w")
            file.write('!')
            file.write('\n\nLast ')
            file.write(str(u1))
            file.write(str(y2))
            file.write('\n\n!')
            file.close()

            f.write('\n')
            f.write(str(u1))
            f.write(str(y2))
            f.write('\n')

            sleep(1)


#Log modules

        elif a == 'openlast':
            print('\nPrinting the last result: ', '\n')
            file = open('last_calculator_result.txt', 'r')
            print(file.read())
            file.close()

            sleep(1)

        elif a == 'openlog':
            print('\nPrinting the last session of the calculator log: ', '\n')
            sleep(0.5)
            f = open('Calculator_log.txt', 'r')
            print(f.read())

            sleep(1)


        else:
            q = 'Unknown input'
            print()
            print('?' * (len(str(q))))
            print(q)
            print('?' * (len(str(q))))

            sleep(1)

    finally:
        f.close()

#TODO:
#division by zero
#dates in python logs
#what was calculating in logs
#yield instead of lists in results
#modules