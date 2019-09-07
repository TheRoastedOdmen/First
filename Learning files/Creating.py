x = str(input('Enter name: '))

x += ".sav"

f = open(x, "a")
f.write("\nSome data\n")

f = open(x, 'r')
print(f.read())
f.close()