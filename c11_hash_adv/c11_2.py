""" c11_2.py """


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
        """ hash function """
        return key % self.bucket_size

    def insert(self, key, value):
        """ insert """
        index = self.get_hash_value(key)
        node = self.buckets[index]
        if node is None:
            self.buckets[index] = Node(key, value)
            return
        prev = node
        while node is not None:
            prev = node
            node = node.ref_next
        prev.ref_next = Node(key, value)

    def search(self, key):
        """ search """
        index = self.get_hash_value(key)
        node = self.buckets[index]
        while node is not None \
            and node.key != key:
            node = node.ref_next
        if node is None:
            return None
        return node.value

    def delete(self, key):
        """ delete """
        index = self.get_hash_value(key)
        node = self.buckets[index]
        prev = None
        while node is not None \
            and node.key != key:
            prev = node
            node = node.ref_next
        if node is None:
            return None
        val = node.value
        if prev is None:
            self.buckets[index] = \
                node.ref_next
        else:
            prev.ref_next = \
                prev.ref_next.ref_next
        return val

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


ht = HashTableChaining()

keys = [27, 82, 18, 42, 25]
for ht_key in keys:
    VALUE = ht_key * 10
    print("insert (key:value)", end="")
    print(f"{ht_key} : {VALUE}")
    ht.insert(ht_key, VALUE)

ht.print_table()

search_keys = [27, 82, 18, 42, 30]
for ht_key in search_keys:
    print("search (key:value)", end=" ")
    print(f"{ht_key} : {ht.search(ht_key)}")

delete_keys = [82, 18]
for ht_key in delete_keys:
    print("delete (key:value)", end=" ")
    print(f"{ht_key} : {ht.delete(ht_key)}")

ht.print_table()
