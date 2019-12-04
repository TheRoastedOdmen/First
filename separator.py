def hello_separated(name = "World", separator = "-"):
    print("Hello", name, sep=separator)

hello_separated()
hello_separated("John")
hello_separated(separator="+++", name="Alice")