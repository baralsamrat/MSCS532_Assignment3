import random

def randomized_quicksort(arr):
    def quicksort(low, high):
        if low < high:
            pivot_index = random.randint(low, high)
            pivot_new_index = partition(low, high, pivot_index)
            quicksort(low, pivot_new_index - 1)
            quicksort(pivot_new_index + 1, high)
    
    def partition(low, high, pivot_index):
        pivot_value = arr[pivot_index]
        arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
        store_index = low
        for i in range(low, high):
            if arr[i] < pivot_value:
                arr[i], arr[store_index] = arr[store_index], arr[i]
                store_index += 1
        arr[store_index], arr[high] = arr[high], arr[store_index]
        return store_index

    quicksort(0, len(arr) - 1)
    return arr
