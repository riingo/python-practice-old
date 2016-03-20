# Implement a hash table in Python.
# Python's dictionary already works as a hash table, but let's implement our
# own for fun. We assume that keys must be integer values, but values can be anything.
# TODO: Should check that key inputs are integers and throw an error if not.

class hashTable:
    def __init__(self, size):
        self.size = size
        self.values = [None] * size     # Initialize an empty table the size given
    def insert(self, key, value):
        hashedKey = key % self.size     # Simple hash function is just key % size to avoid collision
        self.values[hashedKey] = value
    def delete(self, key):              # Delete an entry given the key
        hashedKey = key % self.size 
        self.values[hashedKey] = None
    def findKey(self, value):           # Find the key(s) of entries with the given value.
        keys = []                       # Return the result as a list of keys
        for i in range(self.size):
            if self.values[i] == value:
                keys.append(i)
        return keys
    def findVal(self, key):             # Return the value of an entry with the given key
        hashedKey = key % self.size
        return self.values[hashedKey]
    
        
        
