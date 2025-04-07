# Name: Paris Zhou
# Email: zhou.paris00@gmail.com
# BST and AVL tree
# Date: 2/26/24
# Description: Implementation of a binary search tree. It has multiple methods that allow it to add and remove nodes,
# traverse the tree, and remove subtrees.


import random
from queue_and_stack import Queue, Stack
from bst import BSTNode, BST


class AVLNode(BSTNode):
    """
    AVL Tree Node class. Inherits from BSTNode
    """

    def __init__(self, value: object) -> None:
        """
        Initialize a new AVL node
        """
        # call __init__() from parent class
        super().__init__(value)

        # new variables needed for AVL
        self.parent = None
        self.height = 0

    def __str__(self) -> str:
        """
        Override string method
        """
        return 'AVL Node: {}'.format(self.value)


class AVL(BST):
    """
    AVL Tree class. Inherits from BST
    """

    def __init__(self, start_tree=None) -> None:
        """
        Initialize a new AVL Tree
        """
        # call __init__() from parent class
        super().__init__(start_tree)

    def __str__(self) -> str:
        """
        Override string method
        """
        values = []
        super()._str_helper(self._root, values)
        return "AVL pre-order { " + ", ".join(values) + " }"

    def is_valid_avl(self) -> bool:
        """
        Perform pre-order traversal of the tree. Return False if there
        are any problems with attributes of any of the nodes in the tree.

        This is intended to be a troubleshooting 'helper' method to help
        find any inconsistencies in the tree after the add() or remove()
        operations. Review the code to understand what this method is
        checking and how it determines whether the AVL tree is correct.
        """
        stack = Stack()
        stack.push(self._root)
        while not stack.is_empty():
            node = stack.pop()
            if node:
                # check for correct height (relative to children)
                left = node.left.height if node.left else -1
                right = node.right.height if node.right else -1
                if node.height != 1 + max(left, right):
                    return False

                if node.parent:
                    # parent and child pointers are in sync
                    if node.value < node.parent.value:
                        check_node = node.parent.left
                    else:
                        check_node = node.parent.right
                    if check_node != node:
                        return False
                else:
                    # NULL parent is only allowed on the root of the tree
                    if node != self._root:
                        return False
                stack.push(node.right)
                stack.push(node.left)
        return True

    # ------------------------------------------------------------------ #

    def add(self, value: object) -> None:
        """
        This method calls a helper function for the recursive add method that adds to an AVL tree. It handles if an AVL is empty
        or not then passes the root and value to be added. We choose to use recursion to implement this solution since
        this is an easy way to reference the ancestors of nodes that are inserted or removed.
        """
        if not self._root:
            self._root = AVLNode(value)
            self._root.parent = None
            self._root.height = 0
            return
        self._recursive_add(self._root, None, value)

        return

        pass

    def _recursive_add(self, root: AVLNode, parent: AVLNode, value: object) -> AVLNode:
        """
        This is a helper function that recursively adds to the AVL tree and balances it. It balances the tree every time
        a node is added. It utilizes multiple methods to rebalance the tree. It firstly determines how to
        traverse down the tree by comparing the value to the value of the node the function is currently traversing
        called root. Once it adds a node, it updates the height of the root node before attempting to balance it.
        """

        # If empty, add new node

        if not root:
            node = AVLNode(value)
            node.parent = parent
            node.height = 0
            return node

        # Do not add duplicates

        if value == root.value:
            return root

        #used to traverse tree and place node

        if value < root.value:
            root.left = self._recursive_add(root.left, root, value)
        else:
            root.right = self._recursive_add(root.right, root, value)

        # update height as balancing depends on accurate height

        self._update_height(root)

        # Check for the balance of the tree and balance if necessary
        # Performed recursively because one node being balanced does not guarantee the other parts of the tree
        # to be balanced

        if self._balance_factor(root) > 1:

            if self._balance_factor(root.right) >= 0:
                return self._rotate_left(root)

            else:
                root.right = self._rotate_right(root.right)
                return self._rotate_left(root)

        elif self._balance_factor(root) < -1:
            if self._balance_factor(root.left) <= 0:
                return self._rotate_right(root)
            else:
                root.left = self._rotate_left(root.left)
                return self._rotate_right(root)
        else:
            self._update_height(root)

        return root

    def remove(self, value: object) -> bool:
        """
        Method calls a helper function to complete the removal of nodes in an AVL tree. We choose to use recursion to implement this solution since
        this is an easy way to reference the ancestors of nodes that are inserted or removed.
        """
        if not self._root:
            return False

        self._recursive_remove(self._root, None, value)

        return
        pass

    def _recursive_remove(self, root: AVLNode, parent: AVLNode, value: object) -> AVLNode:
        """
        Recursive helper function to remove values from the AVL tree. it starts by traversing down the tree to find
        the node that needs to be removed. Once we find the node to be removed we cover easy cases and once we exhaust
        cases with only one branch we check for the minimum element larger than what we delete and effectively swap
        their positions so we can remove a leaf node at the end.
        """

        if not root:
            return root

        # find the place we need to put the node

        if value < root.value:
            root.left = self._recursive_remove(root.left, root, value)
        elif value > root.value:
            root.right = self._recursive_remove(root.right, root, value)
        else:

            # Remove the value

            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            else:

                # We swap the positions with the minimum to swim it through the function.

                min = self._get_min_at_node(root.right)
                root.value = min.value
                root.right = self._recursive_remove(root.right, root, min.value)

        if root is None:
            return root

        # update height as balancing depends on accurate height

        self._update_height(root)

        # Check for the balance of the tree and balance if necessary
        # Performed recursively because one node being balanced does not guarantee the other parts of the tree
        # to be balanced

        if self._balance_factor(root) > 1:
            if self._balance_factor(root.right) >= 0:
                return self._rotate_left(root)

            else:
                root.right = self._rotate_right(root.right)
                return self._rotate_left(root)

        elif self._balance_factor(root) < -1:
            if self._balance_factor(root.left) <= 0:
                return self._rotate_right(root)
            else:
                root.left = self._rotate_left(root.left)
                return self._rotate_right(root)
        else:
            self._update_height(root)

        return root

    def _get_min_at_node(self, node: AVLNode) -> AVLNode:
        """
        Find the smallest possible element within one branch of a tree.
        Used to find the minimum element greater than the element we delete.
        Since our implementation of delete swaps the deleted element with the smallest element larger than it.
        """
        if node is None:
            return node
        if node.left is None:
            return node
        return self._get_min_at_node(node.left)

    def _balance_factor(self, node: AVLNode) -> int:
        """
        The balance factor of the AVL tree is checked by comparing right subtree height minus left subtree height. It
        handles if node is none as we don't need to rebalance if the height is 0.
        """
        if node is not None:
            if node.left:
                left_height = node.left.height
            else:
                left_height = -1
            if node.right:
                right_height = node.right.height
            else:
                right_height = -1

            return right_height - left_height
        else:
            return 0
        pass

    def _get_height(self, node: AVLNode) -> int:
        """
        Returns the height of an AVL node.
        """
        return node.height
        pass

    def _rotate_left(self, node: AVLNode) -> AVLNode:
        """
        This method rotates the AVL tree to the left. It is used in balancing the AVL tree.
        """

        # Declare the parent, child, and relation of the left node to the child

        parent = node.parent
        child = node.right
        node.right = child.left

        # Maintain continuity of subtree

        if node.right is not None:
            node.right.parent = node

        # declare the parent and connect the sub tree if not already done

        if node.parent is None:
            child.parent = None

        # maintain continuity between swapped nodes and the rest of the tree

        elif node is parent.left:
            parent.left = child
            child.parent = parent
        else:
            parent.right = child
            child.parent = parent

        node.parent = child
        child.left = node

        if parent is None:
            self._root = child

        # Update the new heights of the swapped nodes

        self._update_height(node)
        self._update_height(child)

        return child

        pass

    def _rotate_right(self, node: AVLNode) -> AVLNode:
        """
        This method rotates the AVL tree to the right. It is used in balancing the AVL tree.

        """

        # Declare the parent, child, and relation of the left node to the child

        parent = node.parent
        child = node.left
        node.left = child.right

        # Maintain continuity of subtree

        if node.left is not None:
            node.left.parent = node

        # declare the parent and connect the sub tree if not already done

        if node.parent is None:
            self._root = child
            child.parent = None

        # maintain continuity between swapped nodes and the rest of the tree

        elif node is parent.right:
            parent.right = child
            child.parent = parent
        else:
            parent.left = child
            child.parent = parent

        node.parent = child
        child.right = node

        # Update the new heights of the swapped nodes

        self._update_height(node)
        self._update_height(child)

        return child
        pass

    def _update_height(self, node: AVLNode) -> None:
        """
        This method updates the height of a node by using the knowledge of the adjacent nodes. It will always be 1
        greater than the height of the tallest subtree.
        """

        # check for the heights of adjacent nodes, update height by being taller than the tallest adjacent node

        if not node.right and not node.left:
            node.height = 0
        elif not node.right and node.left:
            node.height = node.left.height + 1
        elif not node.left and node.right:
            node.height = node.right.height + 1
        elif node.right.height > node.left.height:
            node.height = node.right.height + 1
        else:
            node.height = node.left.height + 1

        pass


# ------------------- BASIC TESTING -----------------------------------------


if __name__ == '__main__':

    print("\nPDF - method add() example 1")
    print("----------------------------")
    test_cases = (
        (1, 2, 3),  # RR
        (3, 2, 1),  # LL
        (1, 3, 2),  # RL
        (3, 1, 2),  # LR
    )
    for case in test_cases:
        tree = AVL(case)
        print(tree)

    print("\nPDF - method add() example 2")
    print("----------------------------")
    test_cases = (
        (10, 20, 30, 40, 50),  # RR, RR
        (10, 20, 30, 50, 40),  # RR, RL
        (30, 20, 10, 5, 1),  # LL, LL
        (30, 20, 10, 1, 5),  # LL, LR
        (5, 4, 6, 3, 7, 2, 8),  # LL, RR
        (range(0, 30, 3)),
        (range(0, 31, 3)),
        (range(0, 34, 3)),
        (range(10, -10, -2)),
        ('A', 'B', 'C', 'D', 'E'),
        (1, 1, 1, 1),
    )
    for case in test_cases:
        tree = AVL(case)
        print('INPUT  :', case)
        print('RESULT :', tree)

    print("\nPDF - method add() example 3")
    print("----------------------------")
    for _ in range(100):
        case = list(set(random.randrange(1, 20000) for _ in range(900)))
        tree = AVL()
        for value in case:
            tree.add(value)
        if not tree.is_valid_avl():
            raise Exception("PROBLEM WITH ADD OPERATION")
    print('add() stress test finished')

    print("\nPDF - method remove() example 1")
    print("-------------------------------")
    test_cases = (
        ((1, 2, 3), 1),  # no AVL rotation
        ((1, 2, 3), 2),  # no AVL rotation
        ((1, 2, 3), 3),  # no AVL rotation
        ((50, 40, 60, 30, 70, 20, 80, 45), 0),
        ((50, 40, 60, 30, 70, 20, 80, 45), 45),  # no AVL rotation
        ((50, 40, 60, 30, 70, 20, 80, 45), 40),  # no AVL rotation
        ((50, 40, 60, 30, 70, 20, 80, 45), 30),  # no AVL rotation
    )
    for case, del_value in test_cases:
        tree = AVL(case)
        print('INPUT  :', tree, "DEL:", del_value)
        tree.remove(del_value)
        print('RESULT :', tree)

    print("\nPDF - method remove() example 2")
    print("-------------------------------")
    test_cases = (
        ((50, 40, 60, 30, 70, 20, 80, 45), 20),  # RR
        ((50, 40, 60, 30, 70, 20, 80, 15), 40),  # LL
        ((50, 40, 60, 30, 70, 20, 80, 35), 20),  # RL
        ((50, 40, 60, 30, 70, 20, 80, 25), 40),  # LR
    )
    for case, del_value in test_cases:
        tree = AVL(case)
        print('INPUT  :', tree, "DEL:", del_value)
        tree.remove(del_value)
        print('RESULT :', tree)

    print("\nPDF - method remove() example 3")
    print("-------------------------------")
    case = range(-9, 16, 2)
    tree = AVL(case)
    for del_value in case:
        print('INPUT  :', tree, del_value)
        tree.remove(del_value)
        print('RESULT :', tree)

    print("\nPDF - method remove() example 4")
    print("-------------------------------")
    case = range(0, 34, 3)
    tree = AVL(case)
    for _ in case[:-2]:
        root_value = tree.get_root().value
        print('INPUT  :', tree, root_value)
        tree.remove(root_value)
        print('RESULT :', tree)

    print("\nPDF - method remove() example 5")
    print("-------------------------------")
    for _ in range(100):
        case = list(set(random.randrange(1, 20000) for _ in range(900)))
        tree = AVL(case)
        for value in case[::2]:
            tree.remove(value)
        if not tree.is_valid_avl():
            raise Exception("PROBLEM WITH REMOVE OPERATION")
    print('remove() stress test finished')

    print("\nPDF - method contains() example 1")
    print("---------------------------------")
    tree = AVL([10, 5, 15])
    print(tree.contains(15))
    print(tree.contains(-10))
    print(tree.contains(15))

    print("\nPDF - method contains() example 2")
    print("---------------------------------")
    tree = AVL()
    print(tree.contains(0))

    print("\nPDF - method inorder_traversal() example 1")
    print("---------------------------------")
    tree = AVL([10, 20, 5, 15, 17, 7, 12])
    print(tree.inorder_traversal())

    print("\nPDF - method inorder_traversal() example 2")
    print("---------------------------------")
    tree = AVL([8, 10, -4, 5, -1])
    print(tree.inorder_traversal())

    print("\nPDF - method find_min() example 1")
    print("---------------------------------")
    tree = AVL([10, 20, 5, 15, 17, 7, 12])
    print(tree)
    print("Minimum value is:", tree.find_min())

    print("\nPDF - method find_min() example 2")
    print("---------------------------------")
    tree = AVL([8, 10, -4, 5, -1])
    print(tree)
    print("Minimum value is:", tree.find_min())

    print("\nPDF - method find_max() example 1")
    print("---------------------------------")
    tree = AVL([10, 20, 5, 15, 17, 7, 12])
    print(tree)
    print("Maximum value is:", tree.find_max())

    print("\nPDF - method find_max() example 2")
    print("---------------------------------")
    tree = AVL([8, 10, -4, 5, -1])
    print(tree)
    print("Maximum value is:", tree.find_max())

    print("\nPDF - method is_empty() example 1")
    print("---------------------------------")
    tree = AVL([10, 20, 5, 15, 17, 7, 12])
    print("Tree is empty:", tree.is_empty())

    print("\nPDF - method is_empty() example 2")
    print("---------------------------------")
    tree = AVL()
    print("Tree is empty:", tree.is_empty())

    print("\nPDF - method make_empty() example 1")
    print("---------------------------------")
    tree = AVL([10, 20, 5, 15, 17, 7, 12])
    print("Tree before make_empty():", tree)
    tree.make_empty()
    print("Tree after make_empty(): ", tree)

    print("\nPDF - method make_empty() example 2")
    print("---------------------------------")
    tree = AVL()
    print("Tree before make_empty():", tree)
    tree.make_empty()
    print("Tree after make_empty(): ", tree)
