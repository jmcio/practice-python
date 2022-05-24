#  my-hashtable.py
#  Practice code added by jmcio 5/21/2022
#  Implement Hash Table

class HashTable:
    def __init__(self, items: int = 10):
        # self.hash_table = [None] * items
        self.hash_table = [[] for _ in range(items)]

    def hashing_func(self,key):
        # return key % len(self.hash_table)
        return hash(key) % len(self.hash_table)

    def insert(self, key, value):
        hash_key = self.hashing_func(key)
        key_exists = False
        bucket = self.hash_table[hash_key]
        for i, kv in enumerate(bucket):
            k, v = kv
            if key == k:
                key_exists = True
                break
        if key_exists:
            bucket[i] = (key, value)
        else:
            bucket.append((key, value))

    def search(self, key):
        hash_key = self.hashing_func(key)
        bucket = self.hash_table[hash_key]
        for i, kv in enumerate(bucket):
            k, v = kv
            if key == k:
                return v

    def delete(self, key):
        hash_key = self.hashing_func(key)
        key_exists = False
        bucket = self.hash_table[hash_key]
        for i, kv in enumerate(bucket):
            k, v = kv
            if key == k:
                key_exists = True
                break
        if key_exists:
            del bucket[i]
            print('Key {} deleted'.format(key))
        else:
            print('Key {} not found'.format(key))



ht = HashTable()
tb = ht.hash_table
print("Hash key for 25: ", ht.hashing_func(25))

ht.insert(10, 'Nepal')
print("Hash table: ", tb)
ht.insert(25, 'USA')
print("Hash table: ", tb)
ht.insert(20, 'India')
print("Hash table: ", tb)
print(ht.search(10))
ht.delete(100)
print("Hash table: ", tb)
ht.delete(10)
print("Hash table: ", tb)

