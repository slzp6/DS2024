""" c10_2.py """


class HashTableOA:
    """ hash table (open addressing) """
    def __init__(self):
        self.size = 10
        self.slots = [None] * self.size
        self.data = [None] * self.size
        self.deleted = "\0"

    def hash_func(self, key, size):
        """ hash function """
        return key % size

    def rehash(self, prev_hash, size):
        """ re-hash function """
        return (prev_hash + 1) % size

    def search(self, key):
        """ search """
        start_slot = self.hash_func(key, len(self.slots))
        pos = start_slot

        while self.slots[pos] is not None:
            if self.slots[pos] == key:
                return self.data[pos]
            pos = self.rehash(pos, len(self.slots))
            if pos == start_slot:
                return None

        return None

    def insert(self, key, data):
        """ insert """
        h_val = self.hash_func(key, len(self.slots))

        if self.slots[h_val] is None \
            or self.slots[h_val] == self.deleted:
            self.slots[h_val] = key
            self.data[h_val] = data
        elif self.slots[h_val] == key:
            self.data[h_val] = data
        else:
            next_s = self.rehash(h_val, len(self.slots))
            while self.slots[next_s] is not None \
                and self.slots[next_s] != self.deleted \
                and self.slots[next_s]!=key:
                next_s = \
                    self.rehash(next_s, len(self.slots))
                if next_s == h_val:
                    return
            if self.slots[next_s] is None \
                or self.slots[next_s] == self.deleted:
                self.slots[next_s] = key
                self.data[next_s] = data
            else:
                self.data[next_s] = data

    def delete(self, key):
        """ delete """
        start_slot = self.hash_func(key, len(self.slots))
        pos = start_slot
        key_in_slot = self.slots[pos]

        while key_in_slot is not None:
            if key_in_slot == key:
                data = self.data[pos]
                self.slots[pos] = self.deleted
                self.data[pos] = self.deleted
                return data
            pos = self.rehash(pos, len(self.slots))
            key_in_slot = self.slots[pos]
            if pos == start_slot:
                return None

        return None

    def print_table(self):
        """ print hash table """
        print("--- hash table ---")
        for i in range(self.size):
            print(i, end=": ")
            if self.slots[i] == "\0":
                print("deleted(_)", end=" ")
            else:
                print(f"{self.slots[i]}", end=" ")
                print(f"({self.data[i]})", end=" ")
            print("")
        print("---")


ht = HashTableOA()

keys = [12, 15, 19, 25, 35]
for ht_key in keys:
    HV = ht_key * 10
    print("insert (key:value)", end=" ")
    print(f"{ht_key} : {HV}")
    ht.insert(ht_key, HV)

ht.print_table()

search_keys = [12, 19, 20, 24]
for ht_key in search_keys:
    print("search (key:value)", end=" ")
    print(f"{ht_key} : {ht.search(ht_key)}")

ht.print_table()

delete_keys = [12, 25]
for ht_key in delete_keys:
    print("delete (key:value)", end=" ")
    print(f"{ht_key} : {ht.delete(ht_key)}")

ht.print_table()
