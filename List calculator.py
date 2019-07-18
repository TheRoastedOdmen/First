import time
#import numpy

print('\nL I S T   C A L C U L A T O R\n')
print('Firstly choose an option')
print('Then input the numbers via enter')
print('Finally press enter to get the result\n')
input('Press enter to continue')

while True:
    print("Options: ")
    print("Input '+' to add numbers")
    print("Input '-' to substract numbers")
    print("Input '*' to multiply numbers")
    print("Input '/' to divide numbers")
    print("Input 'exit' to quit the program")
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
        print('###########################')
        print('\nAddition result:', sum(y), '\n')
        print('###########################')
        time.sleep(1)

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
        print('###########################')
        print('\nSubstraction result:', sum(y), '\n')
        print('###########################')
        time.sleep(1)

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

        print('###########################')
        print('\nMultiplication result:', multi(y), '\n')
        print('###########################')
        time.sleep(1)

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
                #       to append(x)
            except:
                break

        def div(y):
            res = 1
            for x in y:
                res = res * x
            return res

        print('###########################')
        print('\nDivision result:', div(y), '\n')
        print('###########################')
        time.sleep(1)

    else:
        print('\nUnknown input\n')
        time.sleep(1)

        #TODO count # symbol




