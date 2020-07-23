x = (1, "a", "!")
y = (3, "b", "|")
z = (2, "c", "/")

print(sorted({x, y, z}))  # хоть тут и стоят {}, отсортирует всеравно в список ([])

print(sorted([x, y, z], key=lambda item: item[1]))

print(sorted([x, y, z], key=lambda item: item[1], reverse=True))
# todo: item[2]
