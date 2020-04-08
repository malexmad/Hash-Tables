# '''
# Linked List hash table key/value pair
# '''

class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    def __repr__(self):
        return f"<{self.key}, {self.value}>"

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity


    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.

        # Part 1: Hash collisions should be handled with an error warning. (Think about and
        # investigate the impact this will have on the tests)

        # Part 2: Change this so that hash collisions are handled with Linked List Chaining.

        Fill this in.
        '''
        ndx = self._hash_mod(key)

        node = self.storage[ndx]

        if node is None:
            self.storage[ndx] = LinkedPair(key, value)
            return

        prev = node
        if node is not None:
            prev = node
            node = node.next
        prev.next = LinkedPair(key, value)

        # if pair is not None:
        #     if pair.key != key:
        #         print("WARNING: Overwriting value")
        #         pair.key = key
        #     pair.value = value
        #
        # else:
        #     self.storage[ndx] = LinkedPair(key, value)


    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        ndx = self._hash_mod(key)


        if self.storage[ndx] is not None and self.storage[ndx].key == key:
            self.storage[ndx] = None
        else:
            print(f"Key: {key} not found!")


    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        ndx = self._hash_mod(key)
        node = self.storage[ndx]

        while node != None and node.key != key:
            node = node.next

        if node is None:
            return None
        else:
            return node.value

        # if self.storage[ndx] is not None and self.storage[ndx].key == key:
        #     return self.storage[ndx].value
        # else:
        #     return None


    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        self.capacity *= 2

        old_s = self.storage.copy()
        self.storage = [None] * self.capacity

        try:
            for item in old_s:
                self.insert(item[0], item[1])
        except:
            pass


if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    # ht.insert("line_2", "Filled beyond capacity")
    # ht.insert("line_3", "Linked list saves the day!")

    print("____")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    # print(ht.retrieve("line_2"))
    # print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    # print(ht.retrieve("line_2"))
    # print(ht.retrieve("line_3"))

    print("")
