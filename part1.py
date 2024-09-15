import random
# Pivot Selection: Randomly choose the pivot element from the subarray.
# Edge Cases: Handle various cases, such as arrays with repeated elements, empty arrays, and already sorted arrays.
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


def deterministic_quicksort(arr):
    def quicksort(low, high):
        if low < high:
            pivot_new_index = partition(low, high)
            quicksort(low, pivot_new_index - 1)
            quicksort(pivot_new_index + 1, high)
    
    def partition(low, high):
        pivot_value = arr[low]
        left = low + 1
        right = high
        while True:
            while left <= right and arr[left] <= pivot_value:
                left += 1
            while left <= right and arr[right] >= pivot_value:
                right -= 1
            if left > right:
                break
            arr[left], arr[right] = arr[right], arr[left]
        arr[low], arr[right] = arr[right], arr[low]
        return right

    quicksort(0, len(arr) - 1)
    return arr
