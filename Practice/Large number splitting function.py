from time import sleep

x = int(input("x: "))  # large positive int number input
A = []  # Empty list for the results


def splitting(x):
    """Splits the large number into small ones(from 0 to 9)"""
    n = len(A)
    while x > 0:
        A.append(x % 10)
        x //= 10
        n += 1
    for k in range(n//2):  # reversing the list
        A[k], A[n-1-k] = A[n-1-k], A[k]
    sleep(1)


#  Defining tests
def splitting_test1():
    
    print("test #1: ", end="")
    splitting(3654876215)
    print("Ok" if A == [3, 6, 5, 4, 8, 7, 6, 2, 1, 5] else "Fail")


def splitting_test2():
    
    print("test #2: ", end="")
    splitting(10)
    print("Ok" if A == [1, 0] else "Fail")


def splitting_test3():

    print("test #3: ", end="")
    splitting(8)
    print("Ok" if A == [8] else "Fail")


if __name__ == "__main__":
    splitting_test1()
    A = []  # recycling the list
    splitting_test2()
    A = []  # recycling the list
    splitting_test3()
    A = []  # recycling the list

splitting(x)
print('Result: ', A)
A = []  # recycling the list
sleep(10)
