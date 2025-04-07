# Name:Paris Zhou
# Contact Email: zhou.paris00@gmail.com
# Data Structures
# Bag ADT Implementation
# Description: Below is an implementation of a Bag ADT, it is based on a dynamic array but does not share the exact
# same methods. It has its own methods that allow adding elements, removing elements, counting elements, clearing
# elements, and comparison of bags.


from dynamic_array import *

class Bag:
    def __init__(self, start_bag=None):
        """
        Init new bag based on Dynamic Array
          
        """
        self._da = DynamicArray()

        # populate bag with initial values (if provided)
        if start_bag is not None:
            for value in start_bag:
                self.add(value)

    def __str__(self) -> str:
        """
        Return content of stack in human-readable form
        """
        out = "BAG: " + str(self._da.length()) + " elements. ["
        out += ', '.join([str(self._da.get_at_index(_))
                          for _ in range(self._da.length())])
        return out + ']'

    def size(self) -> int:
        """
        Return total number of items currently in the bag
        """
        return self._da.length()

    # -----------------------------------------------------------------------

    def add(self, value: object) -> None:
        """
        This method allows adding to the bag ADT, it uses the dynamic array append() method.
        """
        self._da.append(value)
        return
        pass

    def remove(self, value: object) -> bool:
        """
        This method allows removing from the bag ADT, it uses the dynamic array (remove_at_index) method in a for loop
        the loop will search for values to remove in the bag.
        """
        for indexL in range (self._da.length()):
            if self._da.get_at_index(indexL) == value:
                self._da.remove_at_index(indexL)
                return True
        return False
        pass

    def count(self, value: object) -> int:
        """
        This method searches through the bag ADT and finds how many elements are equal to the inputted value and returns
        an integer with the count.
        """
        counter = 0
        for indexL in range (self._da.length()):
            if self._da.get_at_index(indexL) == value:
                counter +=1
        return counter
        pass

    def clear(self) -> None:
        """
        This method clears the bag ADT by resetting the data to an empty array.
        """
        self._da = DynamicArray()
        pass

    def equal(self, second_bag: "Bag") -> bool:
        """
        This method checks if two bag ADTs are equal in length and count of elements. The bags do not have to be sorted.
        """
        if self._da.length() != second_bag.size():
            return False
        for indexL in range (self._da.length()):
            if self.count(self._da.get_at_index(indexL)) != second_bag.count(self._da.get_at_index(indexL)):
                return False
            else:
                continue
        return True

        pass

    def __iter__(self):
        """
        Creates an iterator for looping for the bag ADT with python dunder methods.
        """
        self._index = 0
        return self
        pass

    def __next__(self):
        """
        Obtains the next value and advances the iterator for the bag ADT.
        """
        try:
            value = self._da.get_at_index(self._index)
        except DynamicArrayException:
            raise StopIteration

        self._index += 1
        return value

        pass


# ------------------- BASIC TESTING -----------------------------------------

if __name__ == "__main__":

    print("\n# add example 1")
    bag = Bag()
    print(bag)
    values = [10, 20, 30, 10, 20, 30]
    for value in values:
        bag.add(value)
    print(bag)

    print("\n# remove example 1")
    bag = Bag([1, 2, 3, 1, 2, 3, 1, 2, 3])
    print(bag)
    print(bag.remove(7), bag)
    print(bag.remove(3), bag)
    print(bag.remove(3), bag)
    print(bag.remove(3), bag)
    print(bag.remove(3), bag)

    print("\n# count example 1")
    bag = Bag([1, 2, 3, 1, 2, 2])
    print(bag, bag.count(1), bag.count(2), bag.count(3), bag.count(4))

    print("\n# clear example 1")
    bag = Bag([1, 2, 3, 1, 2, 3])
    print(bag)
    bag.clear()
    print(bag)

    print("\n# equal example 1")
    bag1 = Bag([10, 20, 30, 40, 50, 60])
    bag2 = Bag([60, 50, 40, 30, 20, 10])
    bag3 = Bag([10, 20, 30, 40, 50])
    bag_empty = Bag()

    print(bag1, bag2, bag3, bag_empty, sep="\n")
    print(bag1.equal(bag2), bag2.equal(bag1))
    print(bag1.equal(bag3), bag3.equal(bag1))
    print(bag2.equal(bag3), bag3.equal(bag2))
    print(bag1.equal(bag_empty), bag_empty.equal(bag1))
    print(bag_empty.equal(bag_empty))
    print(bag1, bag2, bag3, bag_empty, sep="\n")

    bag1 = Bag([100, 200, 300, 200])
    bag2 = Bag([100, 200, 30, 100])
    print(bag1.equal(bag2))

    print("\n# __iter__(), __next__() example 1")
    bag = Bag([5, 4, -8, 7, 10])
    print(bag)
    for item in bag:
        print(item)

    print("\n# __iter__(), __next__() example 2")
    bag = Bag(["orange", "apple", "pizza", "ice cream"])
    print(bag)
    for item in bag:
        print(item)
