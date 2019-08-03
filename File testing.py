file = open('testing.txt', "w")
file.write('1\n')
file.write('2')
file.close()

file = open('testing.txt', "r")
print(file.read())
file.close()