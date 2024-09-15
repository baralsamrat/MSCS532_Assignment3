import unittest
from part2 import HashTable  # Replace 'your_module' with the actual module name

class TestHashTable(unittest.TestCase):
    def setUp(self):
        self.table = HashTable(size=5)

    def test_insert_and_search(self):
        self.table.insert('key1', 'value1')
        self.assertEqual(self.table.search('key1'), 'value1')
        self.table.insert('key2', 'value2')
        self.assertEqual(self.table.search('key2'), 'value2')

    def test_update_value(self):
        self.table.insert('key1', 'value1')
        self.table.insert('key1', 'new_value1')
        self.assertEqual(self.table.search('key1'), 'new_value1')

    def test_delete(self):
        self.table.insert('key1', 'value1')
        self.table.delete('key1')
        self.assertIsNone(self.table.search('key1'))

    def test_load_factor(self):
        self.table.insert('key1', 'value1')
        self.table.insert('key2', 'value2')
        self.table.insert('key3', 'value3')
        self.table.insert('key4', 'value4')
        self.table.insert('key5', 'value5')
        self.assertGreater(self.table.load_factor(), 0.7)

    def test_resize(self):
        initial_size = self.table.size
        for i in range(20):
            self.table.insert(f'key{i}', f'value{i}')
        self.assertGreater(self.table.size, initial_size)

if __name__ == '__main__':
    unittest.main()

import csv
from your_module import randomized_quicksort, HashTable  # Replace 'your_module' with the actual module name

def test_quicksort_on_file(filename):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            arr = list(map(int, row))
            sorted_arr = sorted(arr)
            randomized_quicksort(arr)
            assert arr == sorted_arr, f"Failed for {arr}"
            print(f"Test passed for {arr}")

def test_hashtable_on_data(data):
    table = HashTable(size=5)
    for key, value in data:
        table.insert(key, value)
        assert table.search(key) == value, f"Failed to find {key}"
    print("Hash table tests passed.")

if __name__ == '__main__':
    # Example of testing Randomized Quicksort
    test_quicksort_on_file('data/random_numbers.csv')  # Replace with the path to your CSV file
    
    # Example of testing Hash Table with sample data
    sample_data = [('key1', 'value1'), ('key2', 'value2'), ('key3', 'value3')]
    test_hashtable_on_data(sample_data)
