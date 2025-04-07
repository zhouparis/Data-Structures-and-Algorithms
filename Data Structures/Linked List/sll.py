# Name: Paris Zhou
# Email: zhou.paris00@gmail.com

from SLNode import *


class SLLException(Exception):
    """
    Custom exception class to be used by Singly Linked List
     
    """
    pass


class LinkedList:
    def __init__(self, start_list=None) -> None:
        """
        Initialize new linked list
          
        """
        self._head = SLNode(None)

        # populate SLL with initial values (if provided)
        # before using this feature, implement insert_back() method
        if start_list is not None:
            for value in start_list:
                self.insert_back(value)

    def __str__(self) -> str:
        """
        Return content of singly linked list in human-readable form
          
        """
        out = 'SLL ['
        node = self._head.next
        while node:
            out += str(node.value)
            if node.next:
                out += ' -> '
            node = node.next
        out += ']'
        return out

    def length(self) -> int:
        """
        Return the length of the linked list
          
        """
        length = 0
        node = self._head.next
        while node:
            length += 1
            node = node.next
        return length

    def is_empty(self) -> bool:
        """
        Return True is list is empty, False otherwise
          
        """
        return not self._head.next

    # ------------------------------------------------------------------ #

    def insert_front(self, value: object) -> None:
        """
        TODO: Write this implementation
        """
        if self.is_empty():
            self._head.next = SLNode(value)
            return

        node = SLNode(value)
        node.next = self._head.next
        self._head.next = node

        pass

    def insert_back(self, value: object) -> None:
        """
        TODO: Write this implementation
        """
        if self.is_empty():
            self._head.next = SLNode(value)
            return

        node = self._head.next
        while node.next is not None:
            node = node.next
        node.next = SLNode(value)

        pass

    def insert_at_index(self, index: int, value: object) -> None:
        """
        TODO: Write this implementation
        """
        if index == 0:
            self.insert_front(value)
            return

        length = 1
        node = self._head.next
        while node.next is not None:
            node = node.next
            length += 1

        if index > length or index < 0:
            raise SLLException

        node = self._head.next

        for loop_index in range(0, index - 1):
            node = node.next
            loop_index += 1

        new_node = SLNode(value)
        temp_node = node.next
        node.next = new_node
        new_node.next = temp_node

        return
        pass

    def remove_at_index(self, index: int) -> None:
        """
        TODO: Write this implementation
        """

        if self.is_empty() is True:
            raise SLLException

        if index == 0:
            self._head.next = self._head.next.next
            return

        length = 0
        node = self._head.next
        while node.next is not None:
            length += 1
            node = node.next

        if index > length or index < 0:
            raise SLLException

        node = self._head.next

        for loop_index in range(0, index - 1):
            node = node.next
            loop_index += 1

        node.next = node.next.next

        pass

    def remove(self, value: object) -> bool:
        """
        TODO: Write this implementation
        """

        if self.is_empty() is True:
            return False

        length = 1
        node = self._head.next
        while node.next is not None and node.value != value:
            node = node.next
            length += 1

        if node.value == value:
            index = length - 1
            self.remove_at_index(index)
            return True
        else:
            return False

        pass

    def count(self, value: object) -> int:
        """
        TODO: Write this implementation
        """
        count = 0

        if self.is_empty() is True:
            return count

        node = self._head.next

        while node.next is not None:
            if node.value == value:
                count += 1
            node = node.next

        if node.value == value:
            count += 1

        return count

        pass

    def find(self, value: object) -> bool:
        """
        TODO: Write this implementation
        """

        if self.is_empty() is True:
            return False

        node = self._head.next
        while node.next is not None:
            if node.value == value:
                return True
            node = node.next

        if node.value == value:
            return True
        else:
            return False

        pass

    def slice(self, start_index: int, size: int) -> "LinkedList":
        """
        TODO: Write this implementation
        """

        if self.is_empty() is True:
            raise SLLException

        length = 1
        node = self._head.next
        while node.next is not None:
            node = node.next
            length += 1

        if start_index < 0 or size > length or start_index + size > length or size < 0 or start_index == length:
            raise SLLException

        node = self._head.next

        for loop_index in range(0, start_index):
            node = node.next
            loop_index += 1

        new_linkedlist = LinkedList()

        for loop_index in range(size):
            new_linkedlist.insert_back(node.value)
            node = node.next

        return new_linkedlist

        pass


if __name__ == "__main__":

    print("\n# insert_front example 1")
    test_case = ["A", "B", "C"]
    lst = LinkedList()
    for case in test_case:
        lst.insert_front(case)
        print(lst)

    print("\n# insert_back example 1")
    test_case = ["C", "B", "A"]
    lst = LinkedList()
    for case in test_case:
        lst.insert_back(case)
        print(lst)

    print("\n# insert_at_index example 1")
    lst = LinkedList()
    test_cases = [(0, "A"), (0, "B"), (1, "C"), (3, "D"), (-1, "E"), (5, "F")]
    for index, value in test_cases:
        print("Inserted", value, "at index", index, ": ", end="")
        try:
            lst.insert_at_index(index, value)
            print(lst)
        except Exception as e:
            print(type(e))

    print("\n# remove_at_index example 1")
    lst = LinkedList([1, 2, 3, 4, 5, 6])
    print(f"Initial LinkedList : {lst}")
    for index in [0, 2, 0, 2, 2, -2]:
        print("Removed at index", index, ": ", end="")
        try:
            lst.remove_at_index(index)
            print(lst)
        except Exception as e:
            print(type(e))

    print("\n# remove example 1")
    lst = LinkedList([1, 2, 3, 1, 2, 3, 1, 2, 3])
    print(f"Initial LinkedList, Length: {lst.length()}\n  {lst}")
    for value in [7, 3, 3, 3, 3]:
        print(f"remove({value}): {lst.remove(value)}, Length: {lst.length()}"
              f"\n {lst}")

    print("\n# remove example 2")
    lst = LinkedList([1, 2, 3, 1, 2, 3, 1, 2, 3])
    print(f"Initial LinkedList, Length: {lst.length()}\n  {lst}")
    for value in [1, 2, 3, 1, 2, 3, 3, 2, 1]:
        print(f"remove({value}): {lst.remove(value)}, Length: {lst.length()}"
              f"\n {lst}")

    print("\n# count example 1")
    lst = LinkedList([1, 2, 3, 1, 2, 2])
    print(lst, lst.count(1), lst.count(2), lst.count(3), lst.count(4))

    print("\n# find example 1")
    lst = LinkedList(["Waldo", "Clark Kent", "Homer", "Santa Claus"])
    print(lst)
    print(lst.find("Waldo"))
    print(lst.find("Superman"))
    print(lst.find("Santa Claus"))

    print("\n# slice example 1")
    lst = LinkedList([1, 2, 3, 4, 5, 6, 7, 8, 9])
    ll_slice = lst.slice(1, 3)
    print("Source:", lst)
    print("Start: 1 Size: 3 :", ll_slice)
    ll_slice.remove_at_index(0)
    print("Removed at index 0 :", ll_slice)

    print("\n# slice example 2")
    lst = LinkedList([10, 11, 12, 13, 14, 15, 16])
    print("Source:", lst)
    slices = [(0, 7), (-1, 7), (0, 8), (2, 3), (5, 0), (5, 3), (6, 1), (0, 1),(7,0)]
    for index, size in slices:
        print("Start:", index, "Size:", size, end="")
        try:
            print(" :", lst.slice(index, size))
        except:
            print(" : exception occurred.")

    """Input       : SLL [7575 -> 44839 -> 42012 -> 26860 -> 38691 -> 94255 -> 86722 -> -76986 -> -94854 -> 8577] Slice index 10 size 0"""

    print("\n# slice example 2")
    lst = LinkedList([7575, 44839, 42012, 26860, 38691, 94255, 86722, -76986, -94854, 8577])
    print("Source:", lst)
    slices = [(10, 0)]
    for index, size in slices:
        print("Start:", index, "Size:", size, end="")
        try:
            print(" :", lst.slice(index, size))
        except:
            print(" : exception occurred.")