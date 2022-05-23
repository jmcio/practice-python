#  my-hashtable.py


class HashTable:
    def __init__(self, items: int = 10):
        # self.hash_table = [None] * items
        self.hash_table = [[] for _ in range(items)]

    def hashing_func(self,key):
        # return key % len(self.hash_table)
        return hash(key) % len(self.hash_table)

    def insert(self, key, value):
        hash_key = self.hashing_func(key)
        # self.hash_table[hash_key] = value
        key_exists = False
        bucket = self.hash_table[hash_key]
        for i, kv in enumerate(bucket):
            k, v = kv
            if key == k:
                key_exists = True
                break
            if key_exists:
                bucket[i] = ((key, value))
            else:
                bucket.append((key, value))

    # def search(self):
    #     pass
    #
    # def delete(self):
    #     pass


ht = HashTable()
tb = ht.hash_table
print("Hash key for 25: ", ht.hashing_func(25))

ht.insert(10, 'Nepal')
print("Hash table: ", tb)
ht.insert(25, 'USA')
print("Hash table: ", tb)
ht.insert(20, 'India')
print("Hash table: ", tb)

