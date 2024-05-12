import random

c1,c2 = 0,0

def randomized_quicksort(arr):
    global c1

    if len(arr) <= 1:
        return arr
    else:
        pivot = random.choice(arr)
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        c1+= len(left)+len(right)
        return randomized_quicksort(left) + middle + randomized_quicksort(right)

def quicksort(arr):
    global c2
    
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        c2+= len(left)+len(right)
        return quicksort(left) + [pivot] + quicksort(right)

arr = [1,2,3,4,5,6,7,8,9,10]
arr1 = arr.copy()
 
print("Sorted by randomized way:",randomized_quicksort(arr))
print("Comparisons :", c1)

print("\nSorted by normal way",quicksort(arr1))
print("Comparisons" ,c2)