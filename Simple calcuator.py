print('\n                                    ########################################')
print('                                    ### S I M P L E  C A L C U L A T O R ###')
print('                                    ########################################\n')

while True:
    print("Options: ")
    print("Enter '+' to add two numbers")
    print("Enter '-' to substract two numbers")
    print("Enter '*' to multiply two numbers")
    print("Enter '/' to divide two numbers")
    print("Enter 'exit' to quit the program")
    a = input("\nChoose an option: ")

    if a == "exit":
        break
    elif a == "+":
        print("\nAddition\n")
        x = float(input("Enter a number: "))
        y = float(input("Enter an another number: "))
        z = str(x + y)
        print("The answer is: " + z,'\n')
    elif a == "-":
        print("\nSubstraction\n")
        x = float(input("Enter a number: "))
        y = float(input("Enter an another number: "))
        z = str(x - y)
        print("\nThe answer is: " + z,'\n')
    elif a == "*":
        print("\nMultiplication\n")
        x = float(input("Enter a number: "))
        y = float(input("Enter an another number: "))
        z = str(x * y)
        print("\nThe answer is: " + z,'\n')
    elif a == "/":
        print("\nDivision\n")
        x = float(input("Enter a number: "))
        y = float(input("Enter an another number: "))
        z = str(x / y)
        print("\nThe answer is: " + z,'\n')
    else: print("\nUnknown input\n")