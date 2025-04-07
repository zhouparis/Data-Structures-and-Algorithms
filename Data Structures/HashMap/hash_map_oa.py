# Name: Paris Zhou
# Email: zhou.paris00@gmail.com
# Hashmaps - SC and OA
# Due Date: 3/14/24
# Description: This is my implementation of a open addressing hashmap. Hashmaps are an excellent ADT for adding, reading
# and deleting data. It resolves collisions by probing, which is hashing until an empty bucket or tombstone bucket is
# found.. The buckets are indices in a dynamic array.

from a6_include import (DynamicArray, DynamicArrayException, HashEntry,
                        hash_function_1, hash_function_2)


class HashMap:
    def __init__(self, capacity: int, function) -> None:
        """
        Initialize new HashMap that uses
        quadratic probing for collision resolution
          
        """
        self._buckets = DynamicArray()

        # capacity must be a prime number
        self._capacity = self._next_prime(capacity)
        for _ in range(self._capacity):
            self._buckets.append(None)

        self._hash_function = function
        self._size = 0

    def __str__(self) -> str:
        """
        Override string method to provide more readable output
          
        """
        out = ''
        for i in range(self._buckets.length()):
            out += str(i) + ': ' + str(self._buckets[i]) + '\n'
        return out

    def _next_prime(self, capacity: int) -> int:
        """
        Increment from given number to find the closest prime number
          
        """
        if capacity % 2 == 0:
            capacity += 1

        while not self._is_prime(capacity):
            capacity += 2

        return capacity

    @staticmethod
    def _is_prime(capacity: int) -> bool:
        """
        Determine if given integer is a prime number and return boolean
          
        """
        if capacity == 2 or capacity == 3:
            return True

        if capacity == 1 or capacity % 2 == 0:
            return False

        factor = 3
        while factor ** 2 <= capacity:
            if capacity % factor == 0:
                return False
            factor += 2

        return True

    def get_size(self) -> int:
        """
        Return size of map
          
        """
        return self._size

    def get_capacity(self) -> int:
        """
        Return capacity of map
          
        """
        return self._capacity

    # ------------------------------------------------------------------ #

    def put(self, key: str, value: object) -> None:
        """
        Method adds keys and values to the hashmap. Collisions are resolved using open addressing. If a key is already
        present in the hashmap, its value will be replaced and the size of the map will not change. It operates at an
        amortized O(1) time complexity due to the management of load factor reducing the inefficiency of using the
        while loop to probe. Collision handling is done with open addressing.
        """
        # Resize if the current table load is greater than or equal to 0.5

        if self.table_load() >= 0.5:
            self.resize_table(self._next_prime(2 * self._capacity))

        # Hash the key using hash function and capacity

        hashed_key = self._hash_function(key) % self._capacity

        # Insert only in empty cells or tombstones.

        if self._buckets[hashed_key] is None:
            self._buckets[hashed_key] = HashEntry(key, value)
            self._size += 1
        else:

            # Handle collision using open addressing

            index = 0
            hashed_key = (self._hash_function(key) + index ** 2) % self._capacity
            while self._buckets[hashed_key] is not None:

                # Insert at tombstone if found

                if self._buckets[hashed_key].is_tombstone:
                    self._buckets[hashed_key] = HashEntry(key, value)
                    self._size += 1
                    return

                # Replace key's value if key already present, also do not make duplicates

                if self._buckets[hashed_key].key == key:
                    if self._buckets[hashed_key].value == value:
                        return
                    self._buckets[hashed_key] = HashEntry(key, value)
                    return

                # If key/value pair can't be inserted, hash via quadratic probe and try again

                index += 1
                hashed_key = (self._hash_function(key) + index ** 2) % self._capacity

            # The previous while loop would have skipped any filled buckets or inserted at a tombstone so by now
            # we can safely insert at an empty bucket

            self._buckets[hashed_key] = HashEntry(key, value)
            self._size += 1

            return

        pass

    def resize_table(self, new_capacity: int) -> None:
        """
        Method resizes the hashmap, it uses indirect recursion by calling put in order to maintain an appropriately low
        table load. This method runs in O(n) time complexity. The put method runs in amortized O(1)  time complexity
        due to the management of load factor reducing the inefficiency of using the while loop to probe. This means
        the nested loop is not actually running n^2 times. Collision handling is done with open addressing.
        """

        # If resizing to less than 1, do nothing

        if new_capacity < 1:
            return

        # Catch resizes that are smaller than size of map, put() will handle checking table load.

        if new_capacity < self._size:
            new_capacity = self._next_prime(2 * self._capacity)
            return

        # Ensures that the capacity to be resized to is prime

        if self._is_prime(new_capacity) == False:
            new_capacity = self._next_prime(new_capacity)

        # Save the old keys and values

        old_map = self.get_keys_and_values()

        # make a new empty dynamic array and update capacity

        self._capacity = new_capacity
        self.clear()

        # call put to insert old map values into the new map

        for index in range(old_map.length()):
            self.put(old_map[index][0], old_map[index][1])
        return
        pass

    def table_load(self) -> float:
        """
        Method returns the table load of the hashmap, returning the # of values stored/ # of buckets. it runs in O(1)
        time complexity.
        """
        return self._size / self._capacity
        pass

    def empty_buckets(self) -> int:
        """
        This method looks through the hashmap data and counts how many empty buckets are in the hashmap. It runs in
        O(n) time complexity as it must run through the whole map to determine how many empty buckets there are.
        """
        empty = 0

        # None and Tombstones will be counted as empty as they are open for insertion.

        for index in range(self._buckets.length()):
            if self._buckets[index] is None:
                empty += 1
            elif self._buckets[index].is_tombstone:
                empty += 1
            else:
                continue
        return empty
        pass

    def get(self, key: str) -> object:
        """
        This method retrieves a key from the hashmap if it exists. If no such key exists then it will return, doing
        nothing. It operates at an amortized O(1) time complexity due to the management of load factor reducing the
        inefficiency of using the while loop to probe.
        """
        initial_hash = self._hash_function(key) % self._capacity

        if self._buckets[initial_hash] is not None:
            if self._buckets[initial_hash].key == key and self._buckets[initial_hash].is_tombstone == False:
                return self._buckets[initial_hash].value
            else:
                index = 0
                while self._buckets[initial_hash] is not None:
                    if self._buckets[initial_hash].key == key and self._buckets[initial_hash].is_tombstone == False:
                        return self._buckets[initial_hash].value
                    index += 1
                    initial_hash = (self._hash_function(key) + index ** 2) % self._capacity
                return
        return

        pass

    def contains_key(self, key: str) -> bool:
        """
        This method checks if a key exists within the map. It returns a True if the key is present and a False if the
        key is not present. It operates at an amortized O(1) time complexity due to the management of load factor
        reducing the inefficiency of using the while loop to probe.
        """
        initial_hash = self._hash_function(key) % self._capacity
        if self._buckets[initial_hash] is not None:
            if self._buckets[initial_hash].key == key and self._buckets[initial_hash].is_tombstone == False:
                return True
            else:
                index = 0
                while self._buckets[initial_hash] is not None:
                    if self._buckets[initial_hash].key == key and self._buckets[initial_hash].is_tombstone == False:
                        return True
                    index += 1
                    initial_hash = (self._hash_function(key) + index ** 2) % self._capacity
                return False
        return False

        pass

    def remove(self, key: str) -> None:
        """
        This method removes keys and values from a map by setting their tombstone flag to True. The rest of the hashmap
        will ignore this value when trying to probe for retrieve a value. It operates at an amortized O(1)
        time complexity due to the management of load factor reducing the inefficiency of using the while loop to probe.
        """
        initial_hash = self._hash_function(key) % self._capacity

        if self._buckets[initial_hash] is not None:
            if self._buckets[initial_hash].key == key and self._buckets[initial_hash].is_tombstone == False:
                self._buckets[initial_hash].is_tombstone = True
                self._size -= 1
                return
            else:
                index = 0
                while self._buckets[initial_hash] is not None:
                    if self._buckets[initial_hash].key == key and self._buckets[initial_hash].is_tombstone == False:
                        self._buckets[initial_hash].is_tombstone = True
                        self._size -= 1
                        return
                    elif self._buckets[initial_hash].key == key and self._buckets[initial_hash].is_tombstone == True:
                        return
                    index += 1
                    initial_hash = (self._hash_function(key) + index ** 2) % self._capacity
                return
        return
        pass

    def get_keys_and_values(self) -> DynamicArray:
        """
        This method uses the built in iterator to append key/value pairs as tuples from the map into a dynamic array.
        """
        key_value = DynamicArray()

        for map_value in self:
            key_value.append((map_value.key, map_value.value))

        return key_value

        pass

    def clear(self) -> None:
        """
        This method empties the _buckets datamember to empty the hashmap. it then appends None until the capacity and
        sets the size to zero so the hashmap has a clean start for resizing. It is only used in the resizing method.
        The time complexity is O(n)
        """
        self._buckets = DynamicArray()
        for _ in range(self._capacity):
            self._buckets.append(None)
        self._size = 0
        return
        pass

    def __iter__(self):
        """
        Python dunder method that allows iteration of the hashmap.
        """
        self._index = 0

        return self
        pass

    def __next__(self):
        """
        Python dunder method works with iterator dunder method to allow traversal of the hashmap. It ignores None and
        HashEntry objects where .is_tombstone == True. The nested while loops are limited by the size of the array making
        traversals O(n).
        """
        try:

            value = None
            while value is None:

                # Iterate until a HashEntry object is reached

                while self._buckets[self._index] is None:
                    self._index += 1

                # If the HashEntry object is to be ignored, iterate and continue iteration

                if self._buckets[self._index].is_tombstone == True:
                    self._index += 1
                    continue

                # Nonetype and dead HashEntry objects should be ignored until this point
                # so it is safe to return if this condition passes.

                if self._buckets[self._index].is_tombstone == False:
                    value = self._buckets[self._index]
                    self._index += 1
                    return value

        except DynamicArrayException:
            raise StopIteration

        pass


# ------------------- BASIC TESTING ---------------------------------------- #

if __name__ == "__main__":

    print("\nPDF - put example 1")
    print("-------------------")
    m = HashMap(53, hash_function_1)
    for i in range(150):
        m.put('str' + str(i), i * 100)
        if i % 25 == 24:
            print(m.empty_buckets(), round(m.table_load(), 2), m.get_size(), m.get_capacity())

    print("\nPDF - put example 2")
    print("-------------------")
    m = HashMap(41, hash_function_2)
    for i in range(50):
        m.put('str' + str(i // 3), i * 100)
        if i % 10 == 9:
            print(m.empty_buckets(), round(m.table_load(), 2), m.get_size(), m.get_capacity())

    print("\nPDF - resize example 1")
    print("----------------------")
    m = HashMap(20, hash_function_1)
    m.put('key1', 10)
    print(m.get_size(), m.get_capacity(), m.get('key1'), m.contains_key('key1'))
    m.resize_table(30)
    print(m.get_size(), m.get_capacity(), m.get('key1'), m.contains_key('key1'))
    m.resize_table(9)
    print(m.get_size(), m.get_capacity(), m.get('key1'), m.contains_key('key1'))

    print("\nPDF - resize example 2")
    print("----------------------")
    m = HashMap(75, hash_function_2)
    keys = [i for i in range(25, 1000, 13)]
    for key in keys:
        m.put(str(key), key * 42)
    print(m.get_size(), m.get_capacity())

    for capacity in range(111, 1000, 117):
        m.resize_table(capacity)

        if m.table_load() > 0.5:
            print(f"Check that the load factor is acceptable after the call to resize_table().\n"
                  f"Your load factor is {round(m.table_load(), 2)} and should be less than or equal to 0.5")

        m.put('some key', 'some value')
        result = m.contains_key('some key')
        m.remove('some key')

        for key in keys:
            # all inserted keys must be present
            result &= m.contains_key(str(key))
            # NOT inserted keys must be absent
            result &= not m.contains_key(str(key + 1))
        print(capacity, result, m.get_size(), m.get_capacity(), round(m.table_load(), 2))

    print("\nPDF - table_load example 1")
    print("--------------------------")
    m = HashMap(101, hash_function_1)
    print(round(m.table_load(), 2))
    m.put('key1', 10)
    print(round(m.table_load(), 2))
    m.put('key2', 20)
    print(round(m.table_load(), 2))
    m.put('key1', 30)
    print(round(m.table_load(), 2))

    print("\nPDF - table_load example 2")
    print("--------------------------")
    m = HashMap(53, hash_function_1)
    for i in range(50):
        m.put('key' + str(i), i * 100)
        if i % 10 == 0:
            print(round(m.table_load(), 2), m.get_size(), m.get_capacity())

    print("\nPDF - empty_buckets example 1")
    print("-----------------------------")
    m = HashMap(101, hash_function_1)
    print(m.empty_buckets(), m.get_size(), m.get_capacity())
    m.put('key1', 10)
    print(m.empty_buckets(), m.get_size(), m.get_capacity())
    m.put('key2', 20)
    print(m.empty_buckets(), m.get_size(), m.get_capacity())
    m.put('key1', 30)
    print(m.empty_buckets(), m.get_size(), m.get_capacity())
    m.put('key4', 40)
    print(m.empty_buckets(), m.get_size(), m.get_capacity())

    print("\nPDF - empty_buckets example 2")
    print("-----------------------------")
    m = HashMap(53, hash_function_1)
    for i in range(150):
        m.put('key' + str(i), i * 100)
        if i % 30 == 0:
            print(m.empty_buckets(), m.get_size(), m.get_capacity())

    print("\nPDF - get example 1")
    print("-------------------")
    m = HashMap(31, hash_function_1)
    print(m.get('key'))
    m.put('key1', 10)
    print(m.get('key1'))

    print("\nPDF - get example 2")
    print("-------------------")
    m = HashMap(151, hash_function_2)
    for i in range(200, 300, 7):
        m.put(str(i), i * 10)
    print(m.get_size(), m.get_capacity())
    for i in range(200, 300, 21):
        print(i, m.get(str(i)), m.get(str(i)) == i * 10)
        print(i + 1, m.get(str(i + 1)), m.get(str(i + 1)) == (i + 1) * 10)

    print("\nPDF - contains_key example 1")
    print("----------------------------")
    m = HashMap(11, hash_function_1)
    print(m.contains_key('key1'))
    m.put('key1', 10)
    m.put('key2', 20)
    m.put('key3', 30)
    print(m.contains_key('key1'))
    print(m.contains_key('key4'))
    print(m.contains_key('key2'))
    print(m.contains_key('key3'))
    m.remove('key3')
    print(m.contains_key('key3'))

    print("\nPDF - contains_key example 2")
    print("----------------------------")
    m = HashMap(79, hash_function_2)
    keys = [i for i in range(1, 1000, 20)]
    for key in keys:
        m.put(str(key), key * 42)
    print(m.get_size(), m.get_capacity())
    result = True
    for key in keys:
        # all inserted keys must be present
        result &= m.contains_key(str(key))
        # NOT inserted keys must be absent
        result &= not m.contains_key(str(key + 1))
    print(result)

    print("\nPDF - remove example 1")
    print("----------------------")
    m = HashMap(53, hash_function_1)
    print(m.get('key1'))
    m.put('key1', 10)
    print(m.get('key1'))
    m.remove('key1')
    print(m.get('key1'))
    m.remove('key4')

    print("\nPDF - get_keys_and_values example 1")
    print("------------------------")
    m = HashMap(11, hash_function_2)
    for i in range(1, 6):
        m.put(str(i), str(i * 10))
    print(m.get_keys_and_values())

    m.resize_table(2)
    print(m.get_keys_and_values())

    m.put('20', '200')
    m.remove('1')
    m.resize_table(12)
    print(m.get_keys_and_values())

    print("\nPDF - clear example 1")
    print("---------------------")
    m = HashMap(101, hash_function_1)
    print(m.get_size(), m.get_capacity())
    m.put('key1', 10)
    m.put('key2', 20)
    m.put('key1', 30)
    print(m.get_size(), m.get_capacity())
    m.clear()
    print(m.get_size(), m.get_capacity())

    print("\nPDF - clear example 2")
    print("---------------------")
    m = HashMap(53, hash_function_1)
    print(m.get_size(), m.get_capacity())
    m.put('key1', 10)
    print(m.get_size(), m.get_capacity())
    m.put('key2', 20)
    print(m.get_size(), m.get_capacity())
    m.resize_table(100)
    print(m.get_size(), m.get_capacity())
    m.clear()
    print(m.get_size(), m.get_capacity())

    print("\nPDF - __iter__(), __next__() example 1")
    print("---------------------")
    m = HashMap(10, hash_function_1)
    for i in range(5):
        m.put(str(i), str(i * 10))
    print(m)
    for item in m:
        print('K:', item.key, 'V:', item.value)

    print("\nPDF - __iter__(), __next__() example 2")
    print("---------------------")
    m = HashMap(10, hash_function_2)
    for i in range(5):
        m.put(str(i), str(i * 24))
    m.remove('0')
    m.remove('4')
    print(m)
    for item in m:
        print('K:', item.key, 'V:', item.value)
