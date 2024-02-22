# O(1)

class HashTable:
    def __init__(self,size) -> None:
        self.size = size
        self.table = [[] for _ in range(self.size)]
    def hash_fn(self,key):
        return hash(key) % self.size
    def insert(self, key, val):
        key_hash = self.hash_fn(key)
        key_val = [key, val]
        
        if self.table[key_hash] is None:
            self.table[key_hash] = list([key_val])
            return True
        else:
            for pair in self.table[key_hash]:
                if pair[0] == key:
                    pair[1] = val
                    return True
            self.table[key_hash].append(key_val)
            return True
    def get(self, key):
        key_hash = self.hash_fn(key)
        if self.table[key_hash] is not None:
            for pair in self.table[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return None
    
h = HashTable(5)

h.insert('kari', 13)
print(h.get('kari'))
                