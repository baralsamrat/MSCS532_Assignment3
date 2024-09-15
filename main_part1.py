import sys
import random
from part1 import randomized_quicksort  #Import part 1

def main():
    print("Enter a list of integers separated by spaces:")
    input_string = input().strip()
    if not input_string:
        print("No input provided.")
        return
    
    try:
        arr = list(map(int, input_string.split()))
    except ValueError:
        print("Invalid input. Please enter integers only.\n ")
        return

    print("\n")
    print("Original array:", arr)
    randomized_quicksort(arr)
    print("Sorted array:", arr)
    print("\n")

if __name__ == '__main__':
    main()
