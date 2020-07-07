x = "Hello"
el = []

for i in x:
	el.append(i)

for s in el[:-1]:
	print(s, end=", ")
print(el[-1])
