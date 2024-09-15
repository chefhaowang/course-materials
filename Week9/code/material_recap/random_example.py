import random

# 1. random.random() - Generate a random float between 0 and 1
print("random.random():", random.random())

# 2. random.randint(a, b) - Generate a random integer between 10 and 20
print("random.randint(10, 20):", random.randint(10, 20))

# 3. random.uniform(a, b) - Generate a random float between 5.5 and 10.5
print("random.uniform(5.5, 10.5):", random.uniform(5.5, 10.5))

# 4. random.sample(population, k) - Choose 2 unique elements from the list
choices = ['apple', 'banana', 'cherry', 'date', 'fig']
print("random.sample(['apple', 'banana', 'cherry', 'date', 'fig'], 2):",
      random.sample(choices, 2))

# 5. random.shuffle(x) - Shuffle a list
items = [1, 2, 3, 4, 5]
random.shuffle(items)
print("Shuffled list:", items)

# 6. random.randrange(start, stop[, step]) - Generate a random number between 0 and 10, stepping by 2
print("random.randrange(0, 10, 2):", random.randrange(0, 10, 2))



