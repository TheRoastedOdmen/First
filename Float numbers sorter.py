import time

print('\nFloat numbers sorter\n')
print('Press Enter to start the program')
print('Type "exit" to quit the program')

while True:
    a = input('Press Enter')

    x = [float(i) for i in input('Enter the numbers via space ').split()]

        #Implementation of the sort() function
    def sorter(list):
        for num in range(len(list) -1,0,-1):
            for i in range(num):
                if list[i] > list[i+1]:
                    list[i], list[i+1] = list[i+1], list[i]


    sorter(x)
    print('Result :', x)
    time.sleep(1)