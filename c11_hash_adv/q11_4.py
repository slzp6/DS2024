""" q11_4.py """

import random


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
        while node is not None and node.key != key:
            node = node.ref_next
        if node is None:
            return None
        return node.value

    def delete(self, key):
        """ delete """
        index = self.get_hash_value(key)
        node = self.buckets[index]
        prev = None
        while node is not None and node.key != key:
            prev = node
            node = node.ref_next
        if node is None:
            return None
        val = node.value
        if prev is None:
            self.buckets[index] = node.ref_next
        else:
            prev.ref_next = prev.ref_next.ref_next
        return val

    def count_collisions(self):
        """ find the total number of collisions """
        total = 0
        for i in range(self.bucket_size):
            node = self.buckets[i]
            while node is not None:
                if node.ref_next is not None:
                    total += 1
                node = node.ref_next
        return total

    def print_table(self):
        """ print hash table """
        print("--- hash table ---")
        for i in range(self.bucket_size):
            print(i, end=": ")
            node = self.buckets[i]
            while node is not None:
                print(f"{node.key:2}", end=" ")
                print(f"({node.value:3}) ", end=" ")
                node = node.ref_next
            print("")
        print("---")


ht = HashTableChaining(10)

random.seed(1)
list_keys = random.sample(range(50, 90), 10)

for ht_key in list_keys:
    ht_value = ht_key * 10
    print("insert (key:value) ", ht_key, ":", ht_value)
    ht.insert(ht_key, ht_value)

ht.print_table()

print('item(s): ', len(list_keys))
print('collision(s): ', ht.count_collisions())
