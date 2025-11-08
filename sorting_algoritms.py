def main():
    array1=[]
    array2=[]
    array3=[]
    i=1
    j=600
    k=1
    while len(array1) < 600:
        array1.append(i)
        i=i+1
    print (array1)

    while len(array2) < 600:
        array2.append(j)
        j=j-1
    print (array2)

    first_part(array3)
    print(array3)

    bubble_sort(array1)
    bubble_sort(array2)
    bubble_sort(array3)

    insertion_sort(array1)
    insertion_sort(array2)
    insertion_sort(array3)

    selection_sort(array1)
    selection_sort(array2)
    selection_sort(array3)

    print(merge_sort(array1))
    print(merge_sort(array2))
    print(merge_sort(array3))

    print(quick_sort(array1))
    print(quick_sort(array2))
    print(quick_sort(array3))

    print(heap_sort(array1))
    print(heap_sort(array2))
    print(heap_sort(array3))



    
    
def bubble_sort(array):
    n=len(array)
    for i in range(n):
        swapped=False
        for j in range(0,n-i-1):
            if array[j]>array[j+1]:
                array[j],array[j+1]=array[j+1],array[j]
                swapped=True
        if not swapped:
            break

    print(array)



def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]       # Element to be inserted
        j = i - 1
        # Move elements that are greater than key one position ahead
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key   # Insert key at correct position
        print(arr)

def selection_sort(arr):
    n = len(arr)

    # Move the boundary of unsorted array one by one
    for i in range(n - 1):
        min_index = i  # Assume the current position holds the smallest element

        # Find the smallest element in the remaining unsorted part
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap the found minimum element with the first element of the unsorted part
        arr[i], arr[min_index] = arr[min_index], arr[i]
    print(arr)

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # Find the midpoint
        #slice the array into two halves
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Recursively sort both halves
        merge_sort(left_half)
        merge_sort(right_half)

        # Merge the sorted halves
        i = j = k = 0

        # Compare and copy the smaller element back into arr
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Copy any remaining elements (if any)
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

    return arr

def quick_sort(arr):
    if len(arr) <= 1:
        return arr  # Base case: already sorted if 0 or 1 element

    pivot = arr[len(arr) // 2]  # Choose the middle element as pivot
    left = [x for x in arr if x < pivot]      # Elements less than pivot
    middle = [x for x in arr if x == pivot]   # Elements equal to pivot
    right = [x for x in arr if x > pivot]     # Elements greater than pivot

    # Recursively sort the left and right parts
    return quick_sort(left) + middle + quick_sort(right)


def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    # Make a copy of the original array
    new_arr = arr.copy()
    n = len(new_arr)

    # Build a max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(new_arr, n, i)

    # Extract elements from heap
    for i in range(n - 1, 0, -1):
        new_arr[i], new_arr[0] = new_arr[0], new_arr[i]
        heapify(new_arr, i, 0)

    return new_arr  # Return the sorted array

def first_part(array3):
    k = 1
    while len(array3) < 300:
        array3.append(k)
        k += 1
    second_part(array3)

def second_part(array3):
    a = 600
    while len(array3) < 600:
        array3.append(a)
        a -= 1
    return array3

main()
