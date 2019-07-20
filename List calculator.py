from time import sleep
import math
#import numpy

u = '\nL I S T   C A L C U L A T O R\n'
print('#' * ((len(str(u))) - 2))
print(u)
print('#' * ((len(str(u))) - 2))

print('\nFirstly choose an option')
print('Then input the numbers via enter')
print('When you done inputting press enter to get the result\n')
input('Press enter to continue')

while True:
    print("\n__________OPTIONS___________ \n")
    print("Input '+' to add the numbers")
    print("Input '-' to substract the numbers")
    print("Input '*' to multiply the numbers")
    print("Input '/' to divide the numbers")
    print("Input '**' to exponentiation of a list of numbers")
    print("Input 'y/x to divide 1 number to a list of numbers (also %)")
    print("Input 'x/y to divide a list of number to a 1 number (also %)")
    print("Input '!' to factorial the numbers")
    print("\nInput 'exit' to quit the program")

    a = str(input("\nChoose an option: "))
    n = 1
    y = []
    #np.seterr(divide='ignore')

    if a == "exit":
        break
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
        print('+' * (len(u1) + len(str(sum(y))) + 2), '\n')
        print(u1, sum(y), '\n')
        print('+' * (len(u1) + len(str(sum(y))) + 2))

        sleep(1)

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
        print()
        print('-' * (len(str('Substraction result: ')) + len(str(sum(y)))))
        print('\nSubstraction result:', sum(y), '\n')
        print('-' * (len(str('Substraction result: ')) + len(str(sum(y)))))

        sleep(1)

    elif a == '*':
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

        print()
        print('x' * (len(str('Multiplication result: ')) + len(str(multi(y)))))
        print('\nMultiplication result:', multi(y), '\n')
        print('x' * (len(str('Multiplication result: ')) + len(str(multi(y)))))

        sleep(1)

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

        print()
        print('/' * (len(str('Division result: ')) + len(str(div(y)))))
        print('\nDivision result:', div(y), '\n')
        print('/' * (len(str('Division result: ')) + len(str(div(y)))))

        sleep(1)

    elif a == '**':
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

        y2 = []
        for x in y:
            res = x**v
            y2.append(res)

        print()
        print('^' * (len(str('Exponentiation result: ')) + len(str(y2))))
        print('\nExponentiation result:', y2, '\n')
        print('^' * (len(str('Exponentiation result: ')) + len(str(y2))))

        sleep(1)

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

        y2 = []
        for x in y:
            res = z/x
            y2.append(res)

        print()
        print('/' * (len(str('y/x result: ')) + len(str(y2))))
        print('\ny/x result:', y2, '\n')
        print('/' * (len(str('y/x result: ')) + len(str(y2))))

        y3 = []
        for res in y2:
            res1 = res * 100
            res2 = str(res1) + '%'
            y3.append(res2)

        print()
        print('%' * (len(str('y/x % result:  ')) + len(str(y3))))
        print('\ny/x % result:', y3, '\n')
        print('%' * (len(str('y/x % result:  ')) + len(str(y3))))

        sleep(1)

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

        y2 = []
        for x in y:
            res = x/z1
            y2.append(res)

        print()
        print('/' * (len(str('x/y result: ')) + len(str(y2))))
        print('\nx/y result:', y2, '\n')
        print('/' * (len(str('x/y result: ')) + len(str(y2))))

        y3 = []
        for res in y2:
            res1 = res * 100
            res2 = str(res1) + '%'
            y3.append(res2)

        print()
        print('%' * (len(str('x/y % result:  ')) + len(str(y3))))
        print('\nx/y % result:', y3, '\n')
        print('%' * (len(str('x/y % result:  ')) + len(str(y3))))

        sleep(1)

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

        y2 = []
        for x in y:
            res = math.factorial(x)
            y2.append(res)

        print()
        print('!' * (len(str('Factorial result: ')) + len(str(y2))))
        print('\nFactorial result:', y2, '\n')
        print('!' * (len(str('Factorial result: ')) + len(str(y2))))
        sleep(1)

    else:
        q = 'Unknown input'
        print()
        print('?' * (len(str(q))))
        print(q)
        print('?' * (len(str(q))))

        sleep(1)

#TODO:
#Calculation
#modules
#division by zero




