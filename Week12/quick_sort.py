def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    # Choose a pivot element (typically the first element in the array)
    pivot = arr[0]

    # Partitioning step: separate the array into elements less than and greater than the pivot
    less_than_pivot = [x for x in arr[1:] if x <= pivot]
    greater_than_pivot = [x for x in arr[1:] if x > pivot]

    # Recursively apply quick_sort to the two partitions and return the combined result
    return quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_than_pivot)



arr = [33, 10, 55, 71, 29, 42, 19, 8]
sorted_arr = quick_sort(arr)
print(f"Sorted array: {sorted_arr}")
