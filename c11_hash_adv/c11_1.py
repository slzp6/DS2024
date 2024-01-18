""" c11_1.py """


class Node:
    """ node """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.ref_next = None


class HashTableChaining:
    """ hash table (chaining) """
    def __init__(self, bucket_size=10):
        self.bucket_size = bucket_size
        self.buckets = [None] * self.bucket_size

    def get_hash_value(self, key):
        """ get_hash_value """
        return key % self.bucket_size

    def insert(self, key, value):
        """ insert """
        index = self.get_hash_value(key)
        node = self.buckets[index]
        if node is None:
            self.buckets[index] = \
                Node(key, value)
            return
        prev = node
        while node is not None:
            prev = node
            node = node.ref_next
        prev.ref_next = Node(key, value)

    def print_table(self):
        """ print hash table """
        print("--- hash table ---")
        for i in range(self.bucket_size):
            print(i, end=": ")
            node = self.buckets[i]
            while node is not None:
                print(f"{node.key:2}", end=" ")
                print(f"({node.value:3})", end=" ")
                node = node.ref_next
            print("")
        print("---")


ht = HashTableChaining(10)

keys = [27, 82, 18, 42, 25]
for ht_key in keys:
    VALUE = ht_key * 10
    print("insert (key:value)", end=" ")
    print(f"({ht_key}:{VALUE})")
    ht.insert(ht_key, VALUE)

ht.print_table()
