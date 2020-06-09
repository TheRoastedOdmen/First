print("\n")
x = "|̅̅|"
print(x)
i = 0  # level and iteration counter
m = 10  # max lvl

while i < m - 1:

    x += "̅̅|"
    print(x)
    i += 1

print("\n\n\n")
# pyramid
n = m
s = "    " * (n-1)
x = "| ̅̅ |"
y = "| ̅̅"
print(s, x)
i = 0  # refreshing the counter

while i < m - 1:
    n -= 1
    x += "̅̅ |"
    s = "    " * (n-1)  # why do you have to refresh this i wonder
    print(s, y + x)
    y += "| ̅̅"
    i += 1
