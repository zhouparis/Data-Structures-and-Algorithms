# Name: Paris Zhou
# Email: zhou.paris00@gmail.com
# BST and AVL tree
# 2/26/24
# Description: Implementation of a binary search tree. It has multiple methods that allow it to add and remove nodes,
# traverse the tree, and remove sub trees.


import random
from queue_and_stack import Queue, Stack


class BSTNode:
    """
    Binary Search Tree Node class
     
    """

    def __init__(self, value: object) -> None:
        """
        Initialize a new BST node
        """
        self.value = value  # to store node's data
        self.left = None  # pointer to root of left subtree
        self.right = None  # pointer to root of right subtree

    def __str__(self) -> str:
        """
        Override string method
        """
        return 'BST Node: {}'.format(self.value)


class BST:
    """
    Binary Search Tree class
    """

    def __init__(self, start_tree=None) -> None:
        """
        Initialize new Binary Search Tree
          
        """
        self._root = None

        # populate BST with initial values (if provided)
        # before using this feature, implement add() method
        if start_tree is not None:
            for value in start_tree:
                self.add(value)

    def __str__(self) -> str:
        """
        Override string method; display in pre-order
          
        """
        values = []
        self._str_helper(self._root, values)
        return "BST pre-order { " + ", ".join(values) + " }"

    def _str_helper(self, node: BSTNode, values: []) -> None:
        """
        Helper method for __str__. Does pre-order tree traversal
          
        """
        if not node:
            return
        values.append(str(node.value))
        self._str_helper(node.left, values)
        self._str_helper(node.right, values)

    def get_root(self) -> BSTNode:
        """
        Return root of tree, or None if empty
          
        """
        return self._root

    def is_valid_bst(self) -> bool:
        """
        Perform pre-order traversal of the tree.
        Return False if nodes don't adhere to the bst ordering property.

        This is intended to be a troubleshooting method to help find any
        inconsistencies in the tree after the add() or remove() operations.
        A return of True from this method doesn't guarantee that your tree
        is the 'correct' result, just that it satisfies bst ordering.

          
        """
        stack = Stack()
        stack.push(self._root)
        while not stack.is_empty():
            node = stack.pop()
            if node:
                if node.left and node.left.value >= node.value:
                    return False
                if node.right and node.right.value < node.value:
                    return False
                stack.push(node.right)
                stack.push(node.left)
        return True

    # ------------------------------------------------------------------ #

    def add(self, value: object) -> None:
        """
        This method adds a new value to  the binary search tree. It allows for duplicate values. If a node with the value
        to be added already exists then the new value is added to the right subtree of the node.
        """

        # Check for an empty tree

        if not self._root:
            self._root = BSTNode(value)
            return

        # Traverse the tree iteratively and add the node

        node = self._root
        while True:
            if node.value > value:
                if node.left is None:
                    node.left = BSTNode(value)
                    break
                else:
                    node = node.left
            else:
                if node.right is None:
                    node.right = BSTNode(value)
                    break
                else:
                    node = node.right
        pass

    def remove(self, value: object) -> bool:
        """
        Method utilizes three different methods to remove an element of the binary search tree. It traverses the binary
        search tree in a pre order path, when it finds the node with the value to be removed it removes it based on
        the existence of its children and or sub trees. It utilizes, _remove_no_subtrees, _remove_one_subtree,
        and _remove_two_subtrees
        """

        # check for empty tree

        if not self._root:
            return False

        parent = None
        node = self._root

        # Traverse the tree,  if we need to remove, remove depending on whether children of the targeted node exist

        while node:
            if value == node.value:
                if not node.left and not node.right:
                    self._remove_no_subtrees(parent, node)
                elif not node.left or not node.right:
                    self._remove_one_subtree(parent, node)
                else:
                    self._remove_two_subtrees(parent, node)
                return True
            elif value < node.value:
                parent = node
                node = node.left
            else:
                parent = node
                node = node.right

        return False

        pass

    def _remove_no_subtrees(self, remove_parent: BSTNode, remove_node: BSTNode) -> None:
        """
        Method used in the remove function to remove a node without any children or subtrees.
        """
        # remove node that has no subtrees (no left or right nodes)
        if remove_parent:
            if remove_parent.left == remove_node:
                remove_parent.left = None
            else:
                remove_parent.right = None
        else:
            self._root = None

        pass

    def _remove_one_subtree(self, remove_parent: BSTNode, remove_node: BSTNode) -> None:
        """
        Method used in the remove function to remove a node that has one child or subtree.
        """
        # remove node that has a left or right subtree (only)
        if remove_node.left:
            subtree = remove_node.left
        else:
            subtree = remove_node.right

        if remove_parent:
            if remove_parent.left == remove_node:
                remove_parent.left = subtree
            else:
                remove_parent.right = subtree
        else:
            self._root = subtree

        pass

    def _remove_two_subtrees(self, remove_parent: BSTNode, remove_node: BSTNode) -> None:
        """
        Method used in the remove function to remove a node that has two subtrees or children.
        """
        # the parent does not need to be accessed to remove two sub trees

        successor_parent = remove_node
        successor = remove_node.right

        while successor.left:
            successor_parent = successor
            successor = successor.left

        remove_node.value = successor.value

        if successor_parent.left == successor:
            successor_parent.left = successor.right
        else:
            successor_parent.right = successor.right

        pass

    def contains(self, value: object) -> bool:
        """
        This method traverses the binary search tree and returns a boolean based on the presence of the desired value
        being searched.
        """

        if not self._root:
            return False

        node = self._root

        while node:
            if value == node.value:
                return True
            elif value < node.value:
                node = node.left
            else:
                node = node.right
        return False
        pass

    def inorder_traversal(self) -> Queue:
        """
        Traverses the binary search tree in order. It uses a stack and queue to achieve this. The run time is in O(n)
        The stack keeps track of the traversed subtree and then rebuilds the in order traversal into a queue.
        If the tree is empty it will return an empty Queue.
        """

        if not self._root:
            return Queue()

        node = self._root
        stack = Stack()
        answer_queue = Queue()

        while stack or node:
            if node:
                stack.push(node)
                node = node.left
            else:
                if not stack.is_empty():
                    node = stack.pop()
                    answer_queue.enqueue(node.value)
                    node = node.right
                else:
                    break

        return answer_queue

        pass

    def find_min(self) -> object:
        """
        Method performs an in order traversal of the binary search tree and returns the minimum value.
        """
        if not self._root:
            return None

        # Initate stack and queue to perform in order traversal

        stack = Stack()
        queue = Queue()
        node = self._root
        min = node.value

        # Traverse the entire tree and update whether the value being checked is smaller than the current minimum

        while stack or node:
            if node:
                stack.push(node)
                if min > node.value:
                    min = node.value
                node = node.left
            else:
                if not stack.is_empty():
                    node = stack.pop()
                    queue.enqueue(node.value)
                    if min > node.value:
                        min = node.value
                    node = node.right

                else:
                    break
        return min

        pass

    def find_max(self) -> object:
        """
        Method performs an in order traversal of the binary search tree and returns the maximum value.
        """

        if not self._root:
            return None

        stack = Stack()
        queue = Queue()
        node = self._root
        min = node.value

        # Traverse the entire tree and update whether the value being checked is larger than the current minimum

        while stack or node:
            if node:
                stack.push(node)
                if min < node.value:
                    min = node.value
                node = node.left
            else:
                if not stack.is_empty():
                    node = stack.pop()
                    queue.enqueue(node.value)
                    if min < node.value:
                        min = node.value
                    node = node.right

                else:
                    break
        return min

        pass

    def is_empty(self) -> bool:
        """
        Method that checks the binary search tree root node. If the root node is present then it is not empty and will
        return false. If the root node is None then it will return True.
        """

        if not self._root:
            return True
        else:
            return False

        pass

    def make_empty(self) -> None:
        """
        Method that clears a binary search tree by setting the root node to None if the root node exists. If the tree
        is already empty the method will not do anything and then return.
        """
        if not self._root:
            return
        else:
            self._root = None
            return
        pass


# ------------------- BASIC TESTING -----------------------------------------

if __name__ == '__main__':

    print("\nPDF - method add() example 1")
    print("----------------------------")
    test_cases = (
        (1, 2, 3),
        (3, 2, 1),
        (1, 3, 2),
        (3, 1, 2),
    )
    for case in test_cases:
        tree = BST(case)
        print(tree)

    print("\nPDF - method add() example 2")
    print("----------------------------")
    test_cases = (
        (10, 20, 30, 40, 50),
        (10, 20, 30, 50, 40),
        (30, 20, 10, 5, 1),
        (30, 20, 10, 1, 5),
        (5, 4, 6, 3, 7, 2, 8),
        (range(0, 30, 3)),
        (range(0, 31, 3)),
        (range(0, 34, 3)),
        (range(10, -10, -2)),
        ('A', 'B', 'C', 'D', 'E'),
        (1, 1, 1, 1),
    )
    for case in test_cases:
        tree = BST(case)
        print('INPUT  :', case)
        print('RESULT :', tree)

    print("\nPDF - method add() example 3")
    print("----------------------------")
    for _ in range(100):
        case = list(set(random.randrange(1, 20000) for _ in range(900)))
        tree = BST()
        for value in case:
            tree.add(value)
        if not tree.is_valid_bst():
            raise Exception("PROBLEM WITH ADD OPERATION")
    print('add() stress test finished')

    print("\nPDF - method remove() example 1")
    print("-------------------------------")
    test_cases = (
        ((1, 2, 3), 1),
        ((1, 2, 3), 2),
        ((1, 2, 3), 3),
        ((50, 40, 60, 30, 70, 20, 80, 45), 0),
        ((50, 40, 60, 30, 70, 20, 80, 45), 45),
        ((50, 40, 60, 30, 70, 20, 80, 45), 40),
        ((50, 40, 60, 30, 70, 20, 80, 45), 30),
    )
    for case, del_value in test_cases:
        tree = BST(case)
        print('INPUT  :', tree, "DEL:", del_value)
        tree.remove(del_value)
        print('RESULT :', tree)

    print("\nPDF - method remove() example 2")
    print("-------------------------------")
    test_cases = (
        ((50, 40, 60, 30, 70, 20, 80, 45), 20),
        ((50, 40, 60, 30, 70, 20, 80, 15), 40),
        ((50, 40, 60, 30, 70, 20, 80, 35), 20),
        ((50, 40, 60, 30, 70, 20, 80, 25), 40),
    )
    for case, del_value in test_cases:
        tree = BST(case)
        print('INPUT  :', tree, "DEL:", del_value)
        tree.remove(del_value)
        print('RESULT :', tree)

    print("\nPDF - method remove() example 3")
    print("-------------------------------")
    case = range(-9, 16, 2)
    tree = BST(case)
    for del_value in case:
        print('INPUT  :', tree, del_value)
        tree.remove(del_value)
        print('RESULT :', tree)

    print("\nPDF - method remove() example 4")
    print("-------------------------------")
    case = range(0, 34, 3)
    tree = BST(case)
    for _ in case[:-2]:
        root_value = tree.get_root().value
        print('INPUT  :', tree, root_value)
        tree.remove(root_value)
        if not tree.is_valid_bst():
            raise Exception("PROBLEM WITH REMOVE OPERATION")
        print('RESULT :', tree)

    print("\nPDF - method contains() example 1")
    print("---------------------------------")
    tree = BST([10, 5, 15])
    print(tree.contains(15))
    print(tree.contains(-10))
    print(tree.contains(15))

    print("\nPDF - method contains() example 2")
    print("---------------------------------")
    tree = BST()
    print(tree.contains(0))

    print("\nPDF - method inorder_traversal() example 1")
    print("---------------------------------")
    tree = BST([10, 20, 5, 15, 17, 7, 12])
    print(tree.inorder_traversal())

    print("\nPDF - method inorder_traversal() example 2")
    print("---------------------------------")
    tree = BST([8, 10, -4, 5, -1])
    print(tree.inorder_traversal())

    print("\nPDF - method find_min() example 1")
    print("---------------------------------")
    tree = BST([10, 20, 5, 15, 17, 7, 12])
    print(tree)
    print("Minimum value is:", tree.find_min())

    print("\nPDF - method find_min() example 2")
    print("---------------------------------")
    tree = BST([8, 10, -4, 5, -1])
    print(tree)
    print("Minimum value is:", tree.find_min())

    print("\nPDF - method find_max() example 1")
    print("---------------------------------")
    tree = BST([10, 20, 5, 15, 17, 7, 12])
    print(tree)
    print("Maximum value is:", tree.find_max())

    print("\nPDF - method find_max() example 2")
    print("---------------------------------")
    tree = BST([8, 10, -4, 5, -1])
    print(tree)
    print("Maximum value is:", tree.find_max())

    print("\nPDF - method is_empty() example 1")
    print("---------------------------------")
    tree = BST([10, 20, 5, 15, 17, 7, 12])
    print("Tree is empty:", tree.is_empty())

    print("\nPDF - method is_empty() example 2")
    print("---------------------------------")
    tree = BST()
    print("Tree is empty:", tree.is_empty())

    print("\nPDF - method make_empty() example 1")
    print("---------------------------------")
    tree = BST([10, 20, 5, 15, 17, 7, 12])
    print("Tree before make_empty():", tree)
    tree.make_empty()
    print("Tree after make_empty(): ", tree)

    print("\nPDF - method make_empty() example 2")
    print("---------------------------------")
    tree = BST()
    print("Tree before make_empty():", tree)
    tree.make_empty()
    print("Tree after make_empty(): ", tree)
