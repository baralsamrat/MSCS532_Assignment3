class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]
    
    def hash_function(self, key):
        #  universal hash function family
        return hash(key) % self.size
    
    def insert(self, key, value):
        return None
    
    def search(self, key):
        return None
    
    def delete(self, key):
        return None
