class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        # Your code here
        self.capacity = capacity
        self.storage = [None] * capacity
        self.items = 0

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        return(len(self.storage))

    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here
        return self.items / self.capacity


    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here
        hash = 14695981039346656037
        for x in key:
            hash = hash * 1099511628211
            hash = hash ^ ord(x)

        return hash

    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here
        hash = 5381
        for x in key:
            hash = (( hash << 5) + hash) + ord(x)
        
        return hash & 0xFFFFFFFF

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # Your code here
        # for i, item in enumerate(self.storage):
        #     if item and item.key == key:
        #         self.storage[i].value = value
        #         return
        # self.storage.append(HashTableEntry(key, value))
        # self.items += 1
        # print(f"{self.get_load_factor()}")
        # if self.get_load_factor() > 0.75:
        #     print(f"Resizing from {self.capacity} to {self.capacity * 2}")
        #     self.resize(self.capacity * 2)


        # With 2D array
        key_hash = self.hash_index(key)
        key_value = [key, value]

        if self.storage[key_hash] is None:
            self.storage[key_hash] = list([key_value])
            self.items += 1
        else:
            for i in range(len(self.storage[key_hash])):
                if self.storage[key_hash][i][0] == key:
                    self.storage[key_hash][i][1] = value
                    return
            self.storage[key_hash].append(key_value)
            self.items += 1
        if self.get_load_factor() > 0.75:
            self.resize(self.capacity * 2)

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
        # for i, item in enumerate(self.storage):
        #     if item and item.key == key:
        #         del self.storage[i]
        #         self.items -= 1
        #         return
        # print("Not in hash map")


        # With 2D array
        key_hash = self.hash_index(key)
        print("deleting")
        # if self.storage[key_hash] is None:
        #     print("Not in hash map")
        for i in range(0, len(self.storage[key_hash])):
            print( self.storage[key_hash][i])
            if self.storage[key_hash][i][0] == key:
                del self.storage[key_hash][i]
                self.items -= 1
                return
        # print("Not in hash map")


    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here
        # for i, item in enumerate(self.storage):
        #     if item and item.key == key:
        #         return self.storage[i].value
        # return None


        # With 2D array
        key_hash = self.hash_index(key)
        if self.storage[key_hash] is not None:
            for pair in self.storage[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return None


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here
        # oldStorage = self.storage
        # self.capacity = new_capacity
        # self.storage = [None] * new_capacity

        # for item in oldStorage:
        #     if item:
        #         self.put(item.key, item.value)


        # With 2D array
        oldStorage = self.storage
        self.capacity = new_capacity
        self.storage = [None] * new_capacity

        for thing in oldStorage:
            if thing:
                for item in thing:
                    self.put(item[0], item[1])



if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    # ht.put("line_9", "He took his vorpal sword in hand;")
    # ht.put("line_10", "Long time the manxome foe he sought--")
    # ht.put("line_11", "So rested he by the Tumtum tree")
    # ht.put("line_12", "And stood awhile in thought.")
    # ht.put("line_6", "Random Text.")
    # ht.put("line_13", "Random Text.")
    # ht.put("line_14", "Random Text.")
    # ht.put("line_15", "Random Text.")
    # ht.put("line_16", "Random Text.")
    # ht.put("line_17", "Random Text.")
    # ht.put("line_18", "Random Text.")

    ht.delete("line_1")
    ht.delete("line_2")
    ht.delete("line_3")

    # print("")

    # # Test storing beyond capacity
    # for i in range(1, ht.capacity + 1):
    #     print(ht.get(f"line_{i}"))

    # # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, ht.capacity + 1):
        print(ht.get(f"line_{i}"))

    print("")
