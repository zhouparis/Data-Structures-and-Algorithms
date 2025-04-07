# Name: Paris Zhou
# Email: zhou.paris00@gmail.com


from SLNode import SLNode


class QueueException(Exception):
    """
    Custom exception to be used by Queue class
      
    """
    pass


class Queue:
    def __init__(self):
        """
        Initialize new queue with head and tail nodes
          
        """
        self._head = None
        self._tail = None

    def __str__(self):
        """
        Return content of queue in human-readable form
          
        """
        out = 'QUEUE ['
        if not self.is_empty():
            node = self._head
            out = out + str(node.value)
            node = node.next
            while node:
                out = out + ' -> ' + str(node.value)
                node = node.next
        return out + ']'

    def is_empty(self) -> bool:
        """
        Return True is the queue is empty, False otherwise
          
        """
        return self._head is None

    def size(self) -> int:
        """
        Return number of elements currently in the queue
          
        """
        node = self._head
        length = 0
        while node:
            length += 1
            node = node.next
        return length

    # -----------------------------------------------------------------------

    def enqueue(self, value: object) -> None:
        """
        TODO: Write this implementation
        """

        if self.is_empty():
            self._head = SLNode(value)
            self._tail = self._head
            return

        new_node = SLNode(value)
        self._tail.next = new_node
        self._tail = new_node

        pass

    def dequeue(self) -> object:
        """
        TODO: Write this implementation
        """
        if self.is_empty():
            raise QueueException

        if self._head.next:
            popped_value = self._head.value
            self._head = self._head.next
        else:
            popped_value = self._head.value
            self._head = None
        return popped_value

        pass

    def front(self) -> object:
        """
        TODO: Write this implementation
        """

        if self.is_empty():
            raise QueueException

        if self._head:
            front_value = self._head.value

        return front_value

        pass


# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":

    print("\n# enqueue example 1")
    q = Queue()
    print(q)
    for value in [1, 2, 3, 4, 5]:
        q.enqueue(value)
    print(q)

    print("\n# dequeue example 1")
    q = Queue()
    for value in [1, 2, 3, 4, 5]:
        q.enqueue(value)
    print(q)
    for i in range(6):
        try:
            print(q.dequeue())
        except Exception as e:
            print("No elements in queue", type(e))

    print('\n#front example 1')
    q = Queue()
    print(q)
    for value in ['A', 'B', 'C', 'D']:
        try:
            print(q.front())
        except Exception as e:
            print("No elements in queue", type(e))
        q.enqueue(value)
    print(q)
