class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]
        self.count = 0

    def hash_function(self, key):
        """Simple hash function."""
        return hash(key) % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        for item in self.table[index]:
            if item[0] == key:
                item[1] = value
                return
        self.table[index].append([key, value])
        self.count += 1
        if self.load_factor() > 0.7:
            self.resize()

    def search(self, key):
        index = self.hash_function(key)
        for item in self.table[index]:
            if item[0] == key:
                return item[1]
        return None

    def delete(self, key):
        index = self.hash_function(key)
        for i, item in enumerate(self.table[index]):
            if item[0] == key:
                del self.table[index][i]
                self.count -= 1
                if self.load_factor() < 0.2:
                    self.resize(shrink=True)
                return

    def load_factor(self):
        """Returns the current load factor."""
        return self.count / self.size

    def resize(self, shrink=False):
        """Resize the hash table."""
        new_size = self.size * 2 if not shrink else self.size // 2
        new_size = max(new_size, 1)  # Ensure the size is at least 1
        old_table = self.table
        self.size = new_size
        self.table = [[] for _ in range(new_size)]
        self.count = 0
        for bucket in old_table:
            for key, value in bucket:
                self.insert(key, value)
