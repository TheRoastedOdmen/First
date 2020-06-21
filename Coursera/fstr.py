name = input("Введи свое имя: ")
print(f"Привет, {name}!")
print(b"kek")
print(type(b"kek"))

print()

example_string ="привет"
print(type(example_string))
print(example_string)
encoded_string = example_string.encode(encoding="utf-8")
print(encoded_string)
print(type(encoded_string))
decoded_string = encoded_string.decode()
print(decoded_string)