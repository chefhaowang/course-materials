import numpy as np

# Creating a 2D array
matrix = np.array([[1, 2, 3], [4, 5, 6]])
print(matrix)
# Output:
# [[1 2 3]
#  [4 5 6]]

# operations on these arrays
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

result = arr1 + arr2
print(result)  # Output: [5 7 9]

result = arr1 * arr2
print(result)  # Output: [ 4 10 18]

# high-level mathematical operations
matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[5, 6], [7, 8]])

dot_product = np.dot(matrix1, matrix2)
print(dot_product)
# Output:
# [[19 22]
#  [43 50]]
