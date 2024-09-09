m = [[1] * 5] * 4
m[1][2] = 2
for row in m:
    print(row)

for i in m:
    print(id(i))

for i in m:
    for j in i:
        print(id(j
                 ))

# m = [[1] * 5]
# m.append([1] * 5)
# m.append([1] * 5)
# m.append([1] * 5)

# m[1][2] = 2

# print(m)


# n = 1
# if n<2:
#     n = 3
# else:
#     n = 4

# n = 3 if n<2 else 4


# print(n)
# n = 3

# if n< 2:
#     n = True
# else:
#     n = False
    
# print(n)

# n = True if n < 2  else False
