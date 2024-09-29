import random


def bubble_sort(m: int, n: int) -> list[list[int]]:

    total_elements = m * n
    random_list = [random.randint(0, 100) for _ in range(total_elements)]

    for i in range(len(random_list)):
        for j in range(0, len(random_list) - i - 1):
            if random_list[j] > random_list[j + 1]:
                random_list[j], random_list[j +
                                            1] = random_list[j + 1], random_list[j]

    matrix = []
    for i in range(m):
        row = random_list[i * n:(i + 1) * n]
        matrix.append(row)

    return matrix
