# Name: Paris Zhou
# Email: zhou.paris00@gmail.com


from dynamic_array import *


class StackException(Exception):
    """
    Custom exception to be used by Stack class
      
    """
    pass


class Stack:
    def __init__(self):
        """
        Init new stack based on Dynamic Array
          
        """
        self._da = DynamicArray()

    def __str__(self) -> str:
        """
        Return content of stack in human-readable form
          
        """
        out = "STACK: " + str(self._da.length()) + " elements. ["
        out += ', '.join([str(self._da[i]) for i in range(self._da.length())])
        return out + ']'

    def is_empty(self) -> bool:
        """
        Return True is the stack is empty, False otherwise
          
        """
        return self._da.is_empty()

    def size(self) -> int:
        """
        Return number of elements currently in the stack
          
        """
        return self._da.length()

    # -----------------------------------------------------------------------

    def push(self, value: object) -> None:
        """
        TODO: Write this implementation
        """

        self._da.append(value)
        return

        pass

    def pop(self) -> object:
        """
        TODO: Write this implementation
        """
        if self.is_empty():
            raise StackException

        popped_value = self._da.get_at_index(self._da.length()-1)

        self._da.remove_at_index(self._da.length()-1)

        return popped_value

        pass

    def top(self) -> object:
        """
        TODO: Write this implementation
        """
        if self.is_empty():
            raise StackException

        return self._da.get_at_index(self._da.length()-1)

        pass


# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":

    print("\n# push example 1")
    s = Stack()
    print(s)
    for value in [1, 2, 3, 4, 5]:
        s.push(value)
    print(s)

    print("\n# pop example 1")
    s = Stack()
    try:
        print(s.pop())
    except Exception as e:
        print("Exception:", type(e))
    for value in [1, 2, 3, 4, 5]:
        s.push(value)
    for i in range(6):
        try:
            print(s.pop())
        except Exception as e:
            print("Exception:", type(e))

    print("\n# top example 1")
    s = Stack()
    try:
        s.top()
    except Exception as e:
        print("No elements in stack", type(e))
    s.push(10)
    s.push(20)
    print(s)
    print(s.top())
    print(s.top())
    print(s)
