""" q11_6.py """

import random
import time


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


N = 100_000
RANGE_L = 100_000
RANGE_H = 900_000

BUCKET_A = 100
BUCKET_B = 200_000

ht_a = HashTableChaining(BUCKET_A)
ht_b = HashTableChaining(BUCKET_B)

random.seed(1)
keys = random.sample(range(RANGE_L, RANGE_H), N)
print('item(s): ', len(keys))
print('top5: ', keys[0:5])

ta_start = time.time()
for ht_key in keys:
    ht_value = ht_key * 10
    ht_a.insert(ht_key, ht_value)
ta_end = time.time()

tb_start = time.time()
for ht_key in keys:
    ht_value = ht_key * 10
    ht_b.insert(ht_key, ht_value)
tb_end = time.time()

print("---")
print(f"ht_a [{BUCKET_A:8}] collision(s):", end=" ")
print(ht_a.count_collisions())
print(f"ht_b [{BUCKET_B:8}] collision(s):", end=" ")
print(ht_b.count_collisions())
print("---")
print(f"ht_a: {ta_end - ta_start} (sec.)")
print(f"ht_b: {tb_end - tb_start} (sec.)")
print("---")
print("(ht_a / ht_b):", end=" ")
print(f"{(ta_end - ta_start)/(tb_end - tb_start)}")
