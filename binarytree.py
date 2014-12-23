__author__ = 'Jeremy Turinetti'

class BinaryTree(object):
    def __init__(self, root_value=None):
        if root_value is None:
            self.root = None
        else:
            self.root = _Node(root_value)

    def __insert_node(self, node):
        assert isinstance(node, _Node)
        cur_node = self.root
        done = False
        while not done:
            if node.value > cur_node.value:
                if cur_node.right is None:
                    cur_node.right = node
                    done = True
                else:
                    cur_node = cur_node.right
            else:
                if cur_node.left is None:
                    cur_node.left = node
                    done = True
                else:
                    cur_node = cur_node.left

    def insert_value(self, value):
        node = _Node(value)
        if self.root is None:
            self.root = node
        else:
            self.__insert_node(node)

    def print_tree(self):
        node = self.root
        if self.root is None:
            print("Empty binary tree.")
        else:
            self.__print_tree(node)

    def __print_tree(self, node):
        node.status()
        if node.left is not None:
            self.__print_tree(node.left)
        if node.right is not None:
            self.__print_tree(node.right)

    def depth_first_traversal(self):
        node = self.root
        if self.root is None:
            print("Empty binary tree.")
        else:
            self.__depth_first_traversal(node)

    def __depth_first_traversal(self, node):
        if node.left is not None:
            self.__depth_first_traversal(node.left)
        if node.right is not None:
            self.__depth_first_traversal(node.right)
        print(node.value)

    def breadth_first_traversal(self):
        node = self.root
        if self.root is None:
            print("Empty binary tree.")
        else:
            self.__breadth_first_traversal(node)

    def __breadth_first_traversal(self, node):
        pass  # TODO


class _Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def status(self):
        print("current value: ", self.value)
        if self.left is not None:
            print("  left value: ", self.left.value)
        else:
            print("  left value: NULL")
        if self.right is not None:
            print("  right value: ", self.right.value)
        else:
            print("  right value: NULL")