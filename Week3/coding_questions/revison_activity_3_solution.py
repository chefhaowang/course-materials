list_input = ["hello", "world", "Python", "is", "awesome", "and", "fun"]

short = []
medium = []
long = []

for i in list_input:

    if len(i) > 5:
        long.append(i)
    elif len(i) == 5:
        medium.append(i)
    else:
        short.append(i)

print("short: " + str(short))
print("medium: "+ str(medium))
print("long: "+ str(long))