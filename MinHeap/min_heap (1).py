# Name: Paris Zhou
# OSU Email: zhoup@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: Assignment 5 Minimum Heap implementation
# Due Date: 3/4/24
# Description: Minimum heap implementation, using a dynamic array, math, and iteration, we can make a heap.
# The program contains additional functions heapsort, _percolate_down, and percolate_reforged. The percolate functions
# are used within MinHeap to sink nodes. Heapsort is a function that takes a dynamic array, makes it a valid heap
# structure and then sorts the array in a non ascending order.


from dynamic_array import *


class MinHeapException(Exception):
    """
    Custom exception to be used by MinHeap class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class MinHeap:
    def __init__(self, start_heap=None):
        """
        Initialize a new MinHeap
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._heap = DynamicArray()

        # populate MH with initial values (if provided)
        # before using this feature, implement add() method
        if start_heap:
            for node in start_heap:
                self.add(node)

    def __str__(self) -> str:
        """
        Return MH content in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        heap_data = [self._heap[i] for i in range(self._heap.length())]
        return 'HEAP ' + str(heap_data)

    def add(self, node: object) -> None:
        """
        This method adds a new node to the heap. The heap is implemented with a dynamic array, so we use the dynamic
        array append method to add to the last element of the array. The function runs at an amortized O(log(n)).
        """

        # If the heap is empty, we add the node to be added and return

        if self._heap.is_empty():
            self._heap.append(node)
            return

        # Take note of the index as we will need it to swap

        last_value_index = self._heap.length()
        self._heap.append(node)

        # Find the parent index to prepare for moving up the heap
        parent_index = (last_value_index - 1) // 2

        while True:

            # If the child is greater than the parent, swap them

            if self._heap[parent_index] > self._heap[last_value_index]:
                temp = self._heap[parent_index]

                self._heap.set_at_index(parent_index, self._heap[last_value_index])
                self._heap.set_at_index(last_value_index, temp)

            last_value_index = parent_index
            parent_index = (parent_index - 1) // 2

            # once we reach the root we stop

            if parent_index < 0:
                break
        return
        pass

    def is_empty(self) -> bool:
        """
        Method checks whether the heap is empty or not and returns a boolean. It returns True if the heap is empty and
        False if the heap is not empty. Runs in O(1) time complexity.
        """
        if self._heap.is_empty():
            return True
        else:
            return False

        pass

    def get_min(self) -> object:
        """
        Returns the minimum value of the heap, the node with the highest priority. If the heap is empty it will raise an
        exception MinHeapException. Runs in O(1) time complexity.
        """
        if self._heap.is_empty():
            raise MinHeapException

        return self._heap[0]
        pass

    def remove_min(self) -> object:
        """
        Removes the minimum value of the heap and returns it. It uses _percolate_down to restore the heap to a valid
        heap order. It runs at an amortized O(log(n)).
        """
        # Check if heap is empty

        if self._heap.is_empty():
            raise MinHeapException

        # Remember the value of the first element

        root = self._heap[0]

        # Replace value of first element with value of last element and remove the last element

        self._heap.set_at_index(0, self._heap[self._heap.length() - 1])
        self._heap.remove_at_index(self._heap.length() - 1)

        # Sink the swapped element with our _percolate_down function to restore order to the heap

        _percolate_down(self._heap, 0)

        return root
        pass

    def build_heap(self, da: DynamicArray) -> None:
        """
        Takes an inputted dynamic array and through a series of swaps turns it into a valid heap. It runs at O(n).
        Even though _percolate_down has O(log(n)) run time, and seems to be performed n times. The run time is O(n)
        because the number of operations at each level of the heap can be represented by a taylor series that is
        actually bounded by another function that scales with O(n) complexity so we can conclude that the time
        complexity is actually O(n).
        """

        # Make a deep copy of the dynamic array data inputted
        self._heap = DynamicArray(da)

        # Start at the first invalid heap

        parent = (self._heap.length() // 2) - 1

        while True:
            if parent < 0:
                break

            # Restore heap order at each parent

            _percolate_down(self._heap, parent)
            parent = parent - 1

        return
        pass

    def size(self) -> int:
        """
        Returns the current size of the heap. Runs in O(1). Runs in O(1) time complexity.
        """
        return self._heap.length()
        pass

    def clear(self) -> None:
        """
        Clears the heap of all elements. Makes it empty. Runs in O(1) time complexity.
        """
        self._heap = DynamicArray()
        return
        pass


def heapsort(da: DynamicArray) -> None:
    """
    Heapsort takes an inputted dynamic array and sorts it to obey valid heap order rules. It then sorts the dynamic
    array using a modified version of _percolate_down called _percolate_reforged. It takes the last element and swaps
    it with smallest element at the top. Then it reduces the amount of elements considered for sorting and continue to
    sort until the whole array is in the correct order. It runs in O(nlog(n)) time complexity.
    """

    # Create a valid heap

    parent = (da.length() // 2) - 1

    while True:
        if parent < 0:
            break
        _percolate_down(da, parent)
        parent = parent - 1

    # Keep track of the number of elements sorted and exclude them from rearrangement

    counter = 0

    while counter < da.length():
        # Remember the value of the first element
        root = da[0]

        # Replace value of first element with value of last element and increment the counter to avoid the last element

        da.set_at_index(0, da[da.length() - 1 - counter])
        da.set_at_index(da.length() - 1 - counter, root)

        _percolate_reforged(da, 0, counter)
        counter += 1

    return

    pass


# It's highly recommended that you implement the following optional          #
# function for percolating elements down the MinHeap. You can call           #
# this from inside the MinHeap class. You may edit the function definition.  #

def _percolate_down(da: DynamicArray, parent: int) -> None:
    """
    This method restores valid heap order to a heap implemented with a dynamic array. It is given a dynamic array
    and a parent index for a node. It iteratively swaps the node downward with its smallest child node. This is used
    in remove_min(), where we remove the highest priority element.
        """
    if da.is_empty():
        return

    # If array is not empty, compute right and left child indices and check if they are in bounds

    right_child = 2 * parent + 2
    left_child = 2 * parent + 1
    parent_index = parent

    while left_child < da.length():

        # If the right child does not exist, we don't check for presence of a left child because it should always exist
        # on the leaf layer assuming that the heap fills left to right

        if right_child >= da.length():
            if da[parent_index] >= da[left_child]:
                temp = da[parent_index]
                da.set_at_index(parent_index, da[left_child])
                da.set_at_index(left_child, temp)
                return
            return

        # If the parent node is smaller than both child nodes we have reached the correct spot for now.

        if da[parent_index] <= da[left_child] and da[parent_index] <= da[right_child]:
            return

        # If the left child is smallest, swap with the parent and increment the parent node to the newly swapped
        # position. If the right child is smallest, swap with the right instead.


        if da[right_child] >= da[left_child]:
            temp = da[parent_index]
            da.set_at_index(parent_index, da[left_child])
            da.set_at_index(left_child, temp)
            parent_index = left_child
            right_child = 2 * parent_index + 2
            left_child = 2 * parent_index + 1
            continue
        else:
            temp = da[parent_index]
            da.set_at_index(parent_index, da[right_child])
            da.set_at_index(right_child, temp)
            parent_index = right_child
            right_child = 2 * parent_index + 2
            left_child = 2 * parent_index + 1
            continue

    return


def _percolate_reforged(da: DynamicArray, parent: int, counter) -> None:
    """
    This method restores valid heap order to a heap implemented with a dynamic array. This is used in heapsort(), It is given a dynamic array
    and a parent index for a node, and a counter. It iteratively swaps the node downward with its smallest child node.
    We do not remove the highest priority element and instead swap it and exclude it for consideration for any future swaps.
    """
    if da.is_empty():
        return

    # Counter is passed through with the express purpose of keeping track of how many sorted nodes to exclude from
    # consideration for heapsort.

    # If array is not empty, compute right and left child indices and check if they are in bounds

    right_child = 2 * parent + 2
    left_child = 2 * parent + 1
    parent_index = parent

    while left_child < da.length() - 1 - counter:

        # If the right child does not exist, we don't check for presence of a left child because it should always exist
        # on the leaf layer assuming that the heap fills left to right

        if right_child >= da.length() - 1 - counter:
            if da[parent_index] >= da[left_child]:
                temp = da[parent_index]
                da.set_at_index(parent_index, da[left_child])
                da.set_at_index(left_child, temp)
                return
            return

        # If the parent node is smaller than both child nodes we have reached the correct spot for now.

        if da[parent_index] <= da[left_child] and da[parent_index] <= da[right_child]:
            return

        # If the left child is smallest, swap with the parent and increment the parent node to the newly swapped
        # position. If the right child is smallest, swap with the right instead.

        if da[right_child] >= da[left_child]:
            temp = da[parent_index]
            da.set_at_index(parent_index, da[left_child])
            da.set_at_index(left_child, temp)
            parent_index = left_child
            right_child = 2 * parent_index + 2
            left_child = 2 * parent_index + 1
            continue
        else:
            temp = da[parent_index]
            da.set_at_index(parent_index, da[right_child])
            da.set_at_index(right_child, temp)
            parent_index = right_child
            right_child = 2 * parent_index + 2
            left_child = 2 * parent_index + 1
            continue

    return

    pass


# ------------------- BASIC TESTING -----------------------------------------


if __name__ == '__main__':

    print("\nPDF - add example 1")
    print("-------------------")
    h = MinHeap()
    print(h, h.is_empty())
    for value in range(300, 200, -15):
        h.add(value)
        print(h)

    print("\nPDF - add example 2")
    print("-------------------")
    h = MinHeap(['fish', 'bird'])
    print(h)
    for value in ['monkey', 'zebra', 'elephant', 'horse', 'bear']:
        h.add(value)
        print(h)

    print("\nPDF - is_empty example 1")
    print("-------------------")
    h = MinHeap([2, 4, 12, 56, 8, 34, 67])
    print(h.is_empty())

    print("\nPDF - is_empty example 2")
    print("-------------------")
    h = MinHeap()
    print(h.is_empty())

    print("\nPDF - get_min example 1")
    print("-----------------------")
    h = MinHeap(['fish', 'bird'])
    print(h)
    print(h.get_min(), h.get_min())

    print("\nPDF - remove_min example 1")
    print("--------------------------")
    h = MinHeap([1, 10, 2, 9, 3, 8, 4, 7, 5, 6])
    while not h.is_empty() and h.is_empty() is not None:
        print(h, end=' ')
        print(h.remove_min())

    print("\nPDF - build_heap example 1")
    print("--------------------------")
    da = DynamicArray([100, 20, 6, 200, 90, 150, 300])
    h = MinHeap(['zebra', 'apple'])
    print(h)
    h.build_heap(da)
    print(h)

    print("--------------------------")
    print("Inserting 500 into input DA:")
    da[0] = 500
    print(da)

    print("Your MinHeap:")
    print(h)
    if h.get_min() == 500:
        print("Error: input array and heap's underlying DA reference same object in memory")

    print("\nPDF - heapsort example 1")
    print("------------------------")
    da = DynamicArray([100, 20, 6, 200, 90, 150, 300])
    print(f"Before: {da}")
    heapsort(da)
    print(f"After:  {da}")

    print("\nPDF - heapsort example 2")
    print("------------------------")
    da = DynamicArray(['monkey', 'zebra', 'elephant', 'horse', 'bear'])
    print(f"Before: {da}")
    heapsort(da)
    print(f"After:  {da}")

    print("\nPDF - size example 1")
    print("--------------------")
    h = MinHeap([100, 20, 6, 200, 90, 150, 300])
    print(h.size())

    print("\nPDF - size example 2")
    print("--------------------")
    h = MinHeap([])
    print(h.size())

    print("\nPDF - clear example 1")
    print("---------------------")
    h = MinHeap(['monkey', 'zebra', 'elephant', 'horse', 'bear'])
    print(h)
    print(h.clear())
    print(h)
