print ('Float numbers sorter')

while True:
    x = [float(i) for i in input('Enter the float numbers via space ').split()]


    def sorter(list):
        for num in range(len(list) -1,0,-1):
            for i in range(num):
               if list[i] > list[i+1]:
                   list[i], list[i+1] = list[i+1], list[i]


    sorter(x)
    print('Result :', x)
