print ('10 float numbers sorter')

x0 = float(input ('1: '))
x1 = float(input ('2: '))
x2 = float(input ('3: '))
x3 = float(input ('4: '))
x4 = float(input ('5: '))
x5 = float(input ('6: '))
x6 = float(input ('7: '))
x7 = float(input ('8: '))
x8 = float(input ('9: '))
x9 = float(input ('10: '))

def sorter(list):
    for num in range(len(list) -1,0,-1):
        for i in range(num):
            if list[i] > list[i+1]:
                list[i], list[i+1] = list[i+1], list[i]

a = [x0,x1,x2,x3,x4,x5,x6,x7,x8,x9]
sorter(a)

print(a)