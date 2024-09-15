from part2 import HashTable  # import part2 functions
def main():
    table = HashTable(size=5)
    
    while True:
        print("\nHash Table Operations:")
        print("1. Insert")
        print("2. Search")
        print("3. Delete")
        print("4. Exit")
        choice = input("Enter choice (1/2/3/4): ").strip()
        
        if choice == '1':
            key = input("Enter key: ").strip()
            value = input("Enter value: ").strip()
            table.insert(key, value)
            print(f"Inserted ({key}: {value})")
        
        elif choice == '2':
            key = input("Enter key: ").strip()
            result = table.search(key)
            if result is not None:
                print(f"Value for key '{key}': {result}")
            else:
                print(f"Key '{key}' not found.")
        
        elif choice == '3':
            key = input("Enter key: ").strip()
            table.delete(key)
            print(f"Deleted key '{key}'")
        
        elif choice == '4':
            break
        
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == '__main__':
    main()