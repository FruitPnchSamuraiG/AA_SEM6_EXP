import random

def randomized_quicksort_hoare(arr):
    if len(arr) <= 1:
        return arr, 0
    else:
        pivot_index = random.randint(0, len(arr) - 1)
        pivot = arr[pivot_index]
        left, right = [], []
        swaps = 0

        for i in range(len(arr)):
            if i != pivot_index:
                if arr[i] <= pivot:
                    left.append(arr[i])
                else:
                    right.append(arr[i])
                    swaps += 1  # Increment swaps when moving to right partition

        left_sorted, left_swaps = randomized_quicksort_hoare(left)
        right_sorted, right_swaps = randomized_quicksort_hoare(right)

        return left_sorted + [pivot] + right_sorted, swaps + left_swaps + right_swaps

def quicksort_lomuto(arr):
    if len(arr) <= 1:
        return arr, 0
    else:
        pivot = arr[-1]
        i = 0
        swaps = 0

        for j in range(len(arr) - 1):
            if arr[j] <= pivot:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
                swaps += 1  # Increment swaps when swapping elements

        arr[i], arr[-1] = arr[-1], arr[i]
        pivot_index = i

        left_sorted, left_swaps = quicksort_lomuto(arr[:pivot_index])
        right_sorted, right_swaps = quicksort_lomuto(arr[pivot_index + 1:])

        return left_sorted + [pivot] + right_sorted, swaps + left_swaps + right_swaps

# Example usage and counting swaps:
arr = [1, 5, 3, 8, 2, 7, 4, 6, 9]
sorted_arr_hoare, swaps_hoare = randomized_quicksort_hoare(arr.copy())
sorted_arr_lomuto, swaps_lomuto = quicksort_lomuto(arr.copy())

print("Sorted Array (Hoare Partition Scheme):", sorted_arr_hoare)
print("Number of Swaps (Hoare Partition Scheme):", swaps_hoare)

print("\nSorted Array (Lomuto Partition Scheme):", sorted_arr_lomuto)
print("Number of Swaps (Lomuto Partition Scheme):", swaps_lomuto)
