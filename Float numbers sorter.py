import time

print('\nFloat numbers sorter\n')
print('Press Enter to start the program')
print('Type "exit" to quit the program')

while True:
    a = input()
    if a == 'exit':
        break
    else:
        #Implementation of the sort() function
        x = [float(i) for i in input('Enter the numbers via space ').split()]

        def sorter(list):
            for num in range(len(list) -1,0,-1):
                for i in range(num):
                    if list[i] > list[i+1]:
                       list[i], list[i+1] = list[i+1], list[i]


        sorter(x)
        print('Result :', x)
        time.sleep(1)