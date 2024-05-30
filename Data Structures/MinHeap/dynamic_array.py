# Name:Paris Zhou
# OSU Email: zhoup@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: Assignment 2: Dynamic Array and ADT Implementation
# Due Date: 2/5/24
# Description: The below code is an implementation of a Dynamic array ADT in python. The dynamic array ADT
# has a constructor with size, capacity, and data that contains a StaticArray object with the elements within the
# dynamic array the dynamic array has similar methods to StaticArray where get_at_index() and set_at_index() are
# analogous to  get() and set() methods in StaticArray. But Dynamic array features additional methods that allow
# the array to be modified.


from static_array import StaticArray


class DynamicArrayException(Exception):
    """
    Custom exception class to be used by Dynamic Array
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class DynamicArray:
    def __init__(self, start_array=None):
        """
        Initialize new dynamic array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._size = 0
        self._capacity = 4
        self._data = StaticArray(self._capacity)

        # populate dynamic array with initial values (if provided)
        # before using this feature, implement append() method
        if start_array is not None:
            for value in start_array:
                self.append(value)

    def __str__(self) -> str:
        """
        Return content of dynamic array in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "DYN_ARR Size/Cap: "
        out += str(self._size) + "/" + str(self._capacity) + ' ['
        out += ', '.join([str(self._data[_]) for _ in range(self._size)])
        return out + ']'

    def __iter__(self):
        """
        Create iterator for loop
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._index = 0
        return self

    def __next__(self):
        """
        Obtain next value and advance iterator
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        try:
            value = self[self._index]
        except DynamicArrayException:
            raise StopIteration

        self._index += 1
        return value

    def get_at_index(self, index: int) -> object:
        """
        Return value from given index position
        Invalid index raises DynamicArrayException
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        if index < 0 or index >= self._size:
            raise DynamicArrayException
        return self._data[index]

    def set_at_index(self, index: int, value: object) -> None:
        """
        Store value at given index in the array
        Invalid index raises DynamicArrayException
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        if index < 0 or index >= self._size:
            raise DynamicArrayException
        self._data[index] = value

    def __getitem__(self, index) -> object:
        """
        Same functionality as get_at_index() method above,
        but called using array[index] syntax
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.get_at_index(index)

    def __setitem__(self, index, value) -> None:
        """
        Same functionality as set_at_index() method above,
        but called using array[index] syntax
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.set_at_index(index, value)

    def is_empty(self) -> bool:
        """
        Return True is array is empty / False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._size == 0

    def length(self) -> int:
        """
        Return number of elements stored in array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._size

    def get_capacity(self) -> int:
        """
        Return the capacity of the array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._capacity

    def print_da_variables(self) -> None:
        """
        Print information contained in the dynamic array.
        Used for testing purposes.
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        print(f"Length: {self._size}, Capacity: {self._capacity}, {self._data}")

    # -----------------------------------------------------------------------

    def resize(self, new_capacity: int) -> None:
        """
        This function serves to be used internally and resizes the array. It will not resize the array
        to a negative input or to a capacity smaller than its size.
        """

        # Check for new capacity being of greater size

        if new_capacity <= 0 or new_capacity < self._size:
            return

        # Create new array, update capacity

        new_array = StaticArray(new_capacity)

        # If dynamic array was originally empty, update array data with empty array
        # If dynamic array was not empty, move the data over to the new array and then update array

        if self._size == 0:
            self._capacity = new_capacity
            self._data = new_array
            return
        else:
            old_size = self._size
            self._size = 0
            for loop_index in range(old_size):
                self._size += 1
                new_array.set(loop_index, self.get_at_index(loop_index))
            self._data = new_array
            self._capacity = new_capacity
            return
        pass

    def append(self, value: object) -> None:
        """
        This function doubles the Dynamic array capacity using the resize method if it's already full and then adds a
        value to the end. If the dynamic array is not full then it will add the value to the end of the dynamic array.
        """

        # make room for the new element and update size
        if self._size == self._capacity:
            self.resize(self._capacity * 2)

        self._size += 1
        self.set_at_index(int(self._size) - 1, value)

        return

        pass

    def insert_at_index(self, index: int, value: object) -> None:
        """
        This method allows insertion at an index for the DynamicArray. If the index to be inserted at is greater
        than the size or if the index is less than 0 then it will raise DynamicArrayException. The method checks for
        if the DynamicArray is full first, then it will increase the size of the array if it is. If not, then all values
        are moved over by 1 from the index where the new element will be inserted, and then the element is inserted.
        """
        if index > self._size:
            raise DynamicArrayException

        if index < 0:
            raise DynamicArrayException

        if self._size == self._capacity:
            self.resize(self._capacity * 2)

        self._size += 1
        for loop_index in range(self._size - 2, index - 1, -1):
            self.set_at_index(loop_index + 1, self.get_at_index(loop_index))

        self.set_at_index(index, value)

        pass

    def remove_at_index(self, index: int) -> None:
        """
        This method allows removal of an element from an index in the Dynamic Array. It completes the operations in 
        place.
        """

        # Check for resize conditions, if capacity is greater than 10 and the size of the array is less than 1/4 of
        # the capacity. Then if twice the size is greater than or equal to 10 then it will resize to double the size
        # of the array. If twice the array size is less than 10 it will resize to 10

        if self._capacity > 10:
            if self._size < self._capacity / 4:
                if self._size * 2 >= 10:
                    self.resize(self._size * 2)

                else:
                    self.resize(10)

        # Check for if the index is greater than the size of the array or smaller than 0, if it is out of bounds, raise
        # Exception

        if index < 0:
            raise DynamicArrayException
        if index >= self._size:
            raise DynamicArrayException

        # Overwrite the array backwards

        for loop_index in range(index, self._size - 1):
            self.set_at_index(loop_index, self.get_at_index(loop_index + 1))
        self._size -= 1

        pass

    def slice(self, start_index: int, size: int) -> "DynamicArray":
        """
        With a given starting index and a desired size, the slice() method will return a new dynamic array of the length
        equal to the inputted size from the starting index onwards.
        """

        # Check for if the starting index is out of bounds, if the starts in bounds and slice goes out of bounds,
        # or if the size is out of bounds

        if start_index < 0 or start_index >= self._size:
            raise DynamicArrayException
        if start_index + size > self._size:
            raise DynamicArrayException
        if size < 0 or size > self._size:
            raise DynamicArrayException

        # Create new array, append to new dynamic array the slice from current dynamic array

        new_array = DynamicArray()
        for loop_index in range(start_index, start_index + size):
            new_array.append(self.get_at_index(loop_index))

        return new_array

        pass

    def merge(self, second_da: "DynamicArray") -> None:
        """
        This method takes a second Dynamic array and will append it to the current dynamic array, unless the second 
        dynamic array is empty where the method will simply return.
        """
        if second_da.is_empty():
            return

        for loop_index in range(second_da.length()):
            self.append(second_da.get_at_index(loop_index))
        return
        pass

    def map(self, map_func) -> "DynamicArray":
        """
        This method performs a map function on the entirety of a dynamic array and outputs a new dynamic array with 
        the map function results.
        """
        output = DynamicArray()
        for loop_index in range(self._size):
            output.append(map_func(self.get_at_index(loop_index)))
        return output
        pass

    def filter(self, filter_func) -> "DynamicArray":
        """
        This method uses the filter function to filter a dynamic array. The output will be desired elements that have 
        been filtered from the dynamic array. It is outputted in a new dynamic array.
        """
        output = DynamicArray()

        for loop_index in range(self._size):
            if filter_func(self.get_at_index(loop_index)) is True:
                output.append(self.get_at_index(loop_index))
        return output
        pass

    def reduce(self, reduce_func, initializer=None) -> object:
        """
        This method uses a reducing function to reduce a dynamic array. The output is a singular reduced object.
        """

        # if the array is empty, return the initializer

        if self._size == 0:
            return initializer

        # Starting value changes based on if initializer is None, if it is None, set the initializer to the first value
        # and set the starting value for the loop to an index of 1 so we do not index a value twice.
        # Else, with an initializer already defined we can continue to loop through the array, performing the reduction
        # function

        start_value = 0

        if initializer is None:
            initializer = self.get_at_index(0)
            start_value = 1

        for loop_index in range(start_value, self._size):
            initializer = reduce_func(initializer, self.get_at_index(loop_index))

        return initializer

        pass


def find_mode(arr: DynamicArray) -> tuple[DynamicArray, int]:
    """
    The find_mode method finds the mode within a Dynamic array. It iterates through the array counting the times it has
    seen an element. Because the input is sorted we only have to worry about if the element changes. If the element 
    changes, it updates the current counter and the current compared element. If the running counter equals the max
    counter then the answer dynamic array will be appended to. If the running surpasses the maximum counter, it will wipe
    the dynamic array and add the current mode to the array. The output is a tuple of the list of modes and frequency.
    """
    current = None
    current_counter = 0
    max_counter = 0
    mode = None

    answer_array = DynamicArray()

    for loop_index in range(arr.length()):
        if current == arr.get_at_index(loop_index):
            current_counter += 1
        else:
            current = arr.get_at_index(loop_index)
            current_counter = 1
        if current_counter == max_counter:
            answer_array.append(current)
        if current_counter > max_counter:
            answer_array = DynamicArray()
            max_counter = current_counter
            mode = current
            answer_array.append(mode)

    if mode == None:
        return (arr.get_at_index(0), 1)

    return (answer_array, max_counter)

    pass


# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":

    print("\n# resize - example 1")
    da = DynamicArray()

    # print dynamic array's size, capacity and the contents
    # of the underlying static array (data)
    da.print_da_variables()
    da.resize(8)
    da.print_da_variables()
    da.resize(2)
    da.print_da_variables()
    da.resize(0)
    da.print_da_variables()

    print("\n# resize - example 2")
    da = DynamicArray([1, 2, 3, 4, 5, 6, 7, 8])
    print(da)
    da.resize(20)
    print(da)
    da.resize(4)
    print(da)

    print("\n# resize - example 3")
    da = DynamicArray([1, 2, 3, 4, 5, 6, 7, 8])
    print(da)
    da.resize(2000)
    print(da)
    da.resize(8)
    print(da)

    print("\n# append - example 1")
    da = DynamicArray()
    da.print_da_variables()
    da.append(1)
    da.print_da_variables()
    print(da)

    print("\n# append - example 2")
    da = DynamicArray()
    for i in range(9):
        da.append(i + 101)
        print(da)

    print("\n# append - example 3")
    da = DynamicArray()
    for i in range(600):
        da.append(i)
    print(da.length())
    print(da.get_capacity())

    print("\n# insert_at_index - example 1")
    da = DynamicArray([100])
    print(da)
    da.insert_at_index(0, 200)
    da.insert_at_index(0, 300)
    da.insert_at_index(0, 400)
    print(da)
    da.insert_at_index(3, 500)
    print(da)
    da.insert_at_index(1, 600)
    print(da)

    print("\n# insert_at_index example 2")
    da = DynamicArray()
    try:
        da.insert_at_index(-1, 100)
    except Exception as e:
        print("Exception raised:", type(e))
    da.insert_at_index(0, 200)
    try:
        da.insert_at_index(2, 300)
    except Exception as e:
        print("Exception raised:", type(e))
    print(da)

    print("\n# insert at index example 3")
    da = DynamicArray()
    for i in range(1, 10):
        index, value = i - 4, i * 10
        try:
            da.insert_at_index(index, value)
        except Exception as e:
            print("Cannot insert value", value, "at index", index)
    print(da)

    print("\n# remove_at_index - example 1")
    da = DynamicArray([10, 20, 30, 40, 50, 60, 70, 80])
    print(da)
    da.remove_at_index(0)
    print(da)
    da.remove_at_index(6)
    print(da)
    da.remove_at_index(2)
    print(da)

    print("\n# remove_at_index - example 2")
    da = DynamicArray([1024])
    print(da)
    for i in range(17):
        da.insert_at_index(i, i)
    print(da.length(), da.get_capacity())
    for i in range(16, -1, -1):
        da.remove_at_index(0)
    print(da)

    print("\n# remove_at_index - example 3")
    da = DynamicArray()
    print(da.length(), da.get_capacity())
    [da.append(1) for i in range(100)]  # step 1 - add 100 elements
    print(da.length(), da.get_capacity())
    [da.remove_at_index(0) for i in range(68)]  # step 2 - remove 68 elements
    print(da.length(), da.get_capacity())
    da.remove_at_index(0)  # step 3 - remove 1 element
    print(da.length(), da.get_capacity())
    da.remove_at_index(0)  # step 4 - remove 1 element
    print(da.length(), da.get_capacity())
    [da.remove_at_index(0) for i in range(14)]  # step 5 - remove 14 elements
    print(da.length(), da.get_capacity())
    da.remove_at_index(0)  # step 6 - remove 1 element
    print(da.length(), da.get_capacity())
    da.remove_at_index(0)  # step 7 - remove 1 element
    print(da.length(), da.get_capacity())

    for i in range(14):
        print("Before remove_at_index(): ", da.length(), da.get_capacity(), end="")
        da.remove_at_index(0)
        print(" After remove_at_index(): ", da.length(), da.get_capacity())

    print("\n# remove at index - example 4")
    da = DynamicArray([1, 2, 3, 4, 5])
    print(da)
    for _ in range(5):
        da.remove_at_index(0)
        print(da)

    print("\n# slice example 1")
    da = DynamicArray([1, 2, 3, 4, 5, 6, 7, 8, 9])
    da_slice = da.slice(1, 3)
    print(da, da_slice, sep="\n")
    da_slice.remove_at_index(0)
    print(da, da_slice, sep="\n")

    print("\n# slice example 2")
    da = DynamicArray([10, 11, 12, 13, 14, 15, 16])
    print("SOURCE:", da)
    slices = [(0, 7), (-1, 7), (0, 8), (2, 3), (5, 0), (5, 3), (6, 1), (6, -1)]
    for i, cnt in slices:
        print("Slice", i, "/", cnt, end="")
        try:
            print(" --- OK: ", da.slice(i, cnt))
        except:
            print(" --- exception occurred.")

    print("\n# merge example 1")
    da = DynamicArray([1, 2, 3, 4, 5])
    da2 = DynamicArray([10, 11, 12, 13])
    print(da)
    da.merge(da2)
    print(da)

    print("\n# merge example 2")
    da = DynamicArray([1, 2, 3])
    da2 = DynamicArray()
    da3 = DynamicArray()
    da.merge(da2)
    print(da)
    da2.merge(da3)
    print(da2)
    da3.merge(da)
    print(da3)

    print("\n# map example 1")
    da = DynamicArray([1, 5, 10, 15, 20, 25])
    print(da)
    print(da.map(lambda x: x ** 2))

    print("\n# map example 2")


    def double(value):
        return value * 2


    def square(value):
        return value ** 2


    def cube(value):
        return value ** 3


    def plus_one(value):
        return value + 1


    da = DynamicArray([plus_one, double, square, cube])
    for value in [1, 10, 20]:
        print(da.map(lambda x: x(value)))

    print("\n# filter example 1")


    def filter_a(e):
        return e > 10


    da = DynamicArray([1, 5, 10, 15, 20, 25])
    print(da)
    result = da.filter(filter_a)
    print(result)
    print(da.filter(lambda x: (10 <= x <= 20)))

    print("\n# filter example 2")


    def is_long_word(word, length):
        return len(word) > length


    da = DynamicArray("This is a sentence with some long words".split())
    print(da)
    for length in [3, 4, 7]:
        print(da.filter(lambda word: is_long_word(word, length)))

    print("\n# reduce example 1")
    values = [100, 5, 10, 15, 20, 25]
    da = DynamicArray(values)
    print(da)
    print(da.reduce(lambda x, y: (x // 5 + y ** 2)))
    print(da.reduce(lambda x, y: (x + y ** 2), -1))

    print("\n# reduce example 2")
    da = DynamicArray([100])
    print(da.reduce(lambda x, y: x + y ** 2))
    print(da.reduce(lambda x, y: x + y ** 2, -1))
    da.remove_at_index(0)
    print(da.reduce(lambda x, y: x + y ** 2))
    print(da.reduce(lambda x, y: x + y ** 2, -1))

    print("\n# find_mode - example 1")
    test_cases = (
        [1, 1, 2, 3, 3, 4],
        [1, 2, 3, 4, 5],
        ["Apple", "Banana", "Banana", "Carrot", "Carrot",
         "Date", "Date", "Date", "Eggplant", "Eggplant", "Eggplant",
         "Fig", "Fig", "Grape"]
    )

    for case in test_cases:
        da = DynamicArray(case)
        mode, frequency = find_mode(da)
        print(f"{da}\nMode: {mode}, Frequency: {frequency}\n")

    case = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
    da = DynamicArray()
    for x in range(len(case)):
        da.append(case[x])
        mode, frequency = find_mode(da)
        print(f"{da}\nMode: {mode}, Frequency: {frequency}")
