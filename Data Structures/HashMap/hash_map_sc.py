# Name: Paris Zhou
# Email: zhou.paris00@gmail.com
# Course: CS261 - Data Structures
# Assignment: Assignment 6, Hashmaps - SC and OA
# Due Date: 3/14/24
# Description: This is my implementation of a separate chain hashmap. Hashmaps are an excellent ADT for adding, reading
# and deleting data. It resolves collisions by chaining elements that are added to the hashmap. The buckets are made out
# of linked lists. The program also has a function called find_mode, separate from teh hashmap, which uses the hashmap
# created to find the mode(s) of an unsorted dynamic array..


from a6_include import (DynamicArray, LinkedList,
                        hash_function_1, hash_function_2)


class HashMap:
    def __init__(self,
                 capacity: int = 11,
                 function: callable = hash_function_1) -> None:
        """
        Initialize new HashMap that uses
        separate chaining for collision resolution
          
        """
        self._buckets = DynamicArray()

        # capacity must be a prime number
        self._capacity = self._next_prime(capacity)
        for _ in range(self._capacity):
            self._buckets.append(LinkedList())

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
        Increment from given number and the find the closest prime number
          
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
        Method adds to a hash table. It checks if the table load is greater than 1 first, resizing if the table load is
        greater than 1. Then it will run the key through a hash to find where to put it within the buckets. If the key
        is already found then the key value pair will be attached to a linked list at that location. Else the key value
        pair will be set as the head node of a previously empty linked list. It operates at an amortized O(1)
        time complexity due to the management of load factor reducing the inefficiency of using the while loop to probe.
        """

        # Resize if the table load is greater than 1
        if self.table_load() >= 1.0:
            self.resize_table(self._next_prime(2 * self._capacity))
        # Hash the key using

        hashed_key = self._hash_function(key) % self._capacity

        if self._buckets[hashed_key].contains(key) is not None:
            if self._buckets[hashed_key].contains(key).value == value:
                return
            node = self._buckets[hashed_key]._head
            while node:
                if node.key == key:
                    node.value = value
                    break
                else:
                    node = node.next
            return
        else:
            self._buckets[hashed_key].insert(key, value)
            self._size += 1
        return

        # Increment size and capacity if new key/value is added
        # Do not increment size or capacity if a key/value is replaced

        pass

    def resize_table(self, new_capacity: int) -> None:
        """
        Method resizes the hashmap, it uses indirect recursion by calling put in order to maintain an appropriately low
        table load. This method runs in O(n) time complexity. The put method runs in amortized O(1)  time complexity
        due to the management of load factor reducing the inefficiency of using the while loop to probe. This means
        the nested loop is not actually running n^2 times. Collision handling is done with separate chaining.
        """

        # If resizing to less than 1, do nothing

        if new_capacity < 1:
            return

        # Ensures that the capacity to be resized to is prime

        if self._is_prime(new_capacity) == False:
            new_capacity = self._next_prime(new_capacity)

        # Save the old keys and values

        old_map = self.get_keys_and_values()

        # make a new empty dynamic array

        self._capacity = new_capacity
        self.clear()

        # Copy over old values from the saved hashmap

        for index in range(old_map.length()):

            # Re-hash the keys as we put them into the new hashmap as the capacity has changed

            self.put(old_map[index][0], old_map[index][1])

        return
        pass

    def table_load(self) -> float:
        """
        Method returns the table load of the hashmap, returning the # of values stored/ # of buckets. Runs in O(1)
        time complexity.
        """
        return self._size / self._capacity
        pass

    def empty_buckets(self) -> int:
        """
        This method looks through the hashmap data and counts how many empty buckets are in the hashmap. Runs in O(n)
        time complexity.
        """

        empty = 0

        # Skip buckets that have items and count empty buckets

        for index in range(self._buckets.length()):
            if self._buckets[index]._head is None:
                empty += 1
            else:
                continue

        return empty

        pass

    def get(self, key: str):
        """
        This method retrieves a key from the hashmap if it exists. If no such key exists then it will return None.
        Runs in O(1) time complexity amortized. Load factor management keeps .contains() at a constant and prevents
        worst case chaining of length n.
        """

        if self._buckets[self._hash_function(key) % self._capacity]._head is not None:
            if self._buckets[self._hash_function(key) % self._capacity].contains(key) is not None:
                return self._buckets[self._hash_function(key) % self._capacity].contains(key).value
            else:
                return None
        else:
            return None
        pass

    def contains_key(self, key: str) -> bool:
        """
        Method returns a boolean based on whether a key exists within the hashmap. Runs in O(1) time complexity
        amortized. Load factor management keeps .contains() at a constant and prevents worst case chaining of length n.
        """
        if self._buckets[self._hash_function(key) % self._capacity]._head is not None:
            if self._buckets[self._hash_function(key) % self._capacity].contains(key) is not None:
                return True
            else:
                return False
        else:
            return False
        pass

    def remove(self, key: str) -> None:
        """
        This method removes a key from the hashmap if it is present. If a key is removed it will decrement the size.
        Runs in O(1) time complexity amortized. Load factor management keeps .remove() at a constant and prevents
        worst case chaining of length n.
        """
        if self._buckets[self._hash_function(key) % self._capacity]._head is not None:
            if self._buckets[self._hash_function(key) % self._capacity].remove(key):
                self._buckets[self._hash_function(key) % self._capacity].remove(key)
                self._size -= 1
        return

        pass

    def get_keys_and_values(self) -> DynamicArray:
        """
        This method takes the key/value pairs in a hashmap and records them in a dynamic array. It's used in the resize
        method to retain old key/value pairs when resizing the hashmap. Runs in O(n) time complexity amortized.
        """

        # New empty array

        key_value = DynamicArray()

        # Go through the old array

        for index in range(self._buckets.length()):

            # Skip empty memory, we don't have pointers in python

            if self._buckets[index]._head is None:
                continue

            # If there's more than 1 element in the linked list get every value

            if self._buckets[index].length() > 1:
                node = self._buckets[index]._head
                while node:
                    key_value.append((node.key, node.value))
                    node = node.next
            else:
                if self._buckets[index]._head is None:
                    continue
                key_value.append((self._buckets[index]._head.key, self._buckets[index]._head.value))

        return key_value

        pass

    def clear(self) -> None:
        """
        This method empties the existing Hashmap without changing its capacity. Runs in O(n) time complexity.
        """
        self._buckets = DynamicArray()
        for _ in range(self._capacity):
            self._buckets.append(LinkedList())
        self._size = 0
        return
        pass


def find_mode(da: DynamicArray) -> tuple[DynamicArray, int]:
    """
    This method takes an unsorted dynamic array and find the mode(s), it returns a tuple with the mode(s) and the
    frequencies of the mode(s). This method runs at O(n) time complexity.
    """

    # Use hashmap to record values
    map = HashMap()

    # Keys represent the array elements, the value pairs will be the count for how often the key occurs.
    # If the element is already recorded the count is updated. Else, a new entry is created.

    # O(n) time complexity as methods used are O(1)

    for index in range(da.length()):
        if map.get(da[index]):
            map.put(da[index], map.get(da[index]) + 1)
        else:
            map.put(da[index], 1)

    # Iterate through the key/value pairs to find the most repeated elements

    values = map.get_keys_and_values()
    mode = DynamicArray()
    mode_counter = 0

    # Find highest frequency

    for index in range(values.length()):
        if values[index][1] > mode_counter:
            mode_counter = values[index][1]

    # Only add to the answer array if the frequency of an element is equal to the highest frequency in the array

    for index in range(values.length()):
        if values[index][1] == mode_counter:
            mode.append(values[index][0])

    return mode, mode_counter


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

    print("\nPDF - resize example 2")
    print("----------------------")
    m = HashMap(75, hash_function_2)
    keys = [i for i in range(1, 1000, 13)]
    for key in keys:
        m.put(str(key), key * 42)
    print(m.get_size(), m.get_capacity())

    for capacity in range(111, 1000, 117):
        m.resize_table(capacity)

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
    m = HashMap(53, hash_function_1)
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

    m.put('20', '200')
    m.remove('1')
    m.resize_table(2)
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

    print("\nPDF - find_mode example 1")
    print("-----------------------------")
    da = DynamicArray(["apple", "apple", "grape", "melon", "peach"])
    mode, frequency = find_mode(da)
    print(f"Input: {da}\nMode : {mode}, Frequency: {frequency}")

    print("\nPDF - find_mode example 2")
    print("-----------------------------")
    test_cases = (
        ["Arch", "Manjaro", "Manjaro", "Mint", "Mint", "Mint", "Ubuntu", "Ubuntu", "Ubuntu"],
        ["one", "two", "three", "four", "five"],
        ["2", "4", "2", "6", "8", "4", "1", "3", "4", "5", "7", "3", "3", "2"]
    )

    for case in test_cases:
        da = DynamicArray(case)
        mode, frequency = find_mode(da)
        print(f"Input: {da}\nMode : {mode}, Frequency: {frequency}\n")
