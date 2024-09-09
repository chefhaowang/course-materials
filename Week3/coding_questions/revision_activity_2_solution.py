string = "I love Python"

# positive dir
for i in range(0, len(string)):
    print(string[i])

# reverse dir
for i in range(-1, -len(string)-1, -1):
    print(string[i])


i = -1
while i > -len(string)-1:
    print(string[i])
    i -= 1


print(string[::-1])
