def matryoshka (n):
    if n == 1:
        print("Matryoshka")
    else:
        print("Upper level of matryoshka n =", n)
        matryoshka(n-1)
        print("Lower level of matryoshka n =", n)

matryoshka(5)