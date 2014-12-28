__author__ = 'Jeremy Turinetti'

class BinaryTree(object):
    def __init__(self, root_value=None):
        self.height = 0
        self.left_height = 0
        self.right_height = 0

        if root_value is None:
            self.root = None
        else:
            self.root = _Node(root_value)

    def __insert(self, node):
        assert isinstance(node, _Node)
        cur_node = self.root
        cur_height = 0
        done = False

        while not done:
            cur_height = cur_height + 1
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

        if cur_height > self.height:
            self.height = cur_height

    def insert(self, value):
        node = _Node(value)
        if self.root is None:
            self.root = node
        else:
            self.__insert(node)

    def balance_tree(self):
        pass # TODO

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
        if node is None:
            print("Empty binary tree.")
        else:
            self.__depth_first_traversal(node)

    def __depth_first_traversal(self, node):
        if node.left is not None:
            self.__depth_first_traversal(node.left)
        if node.right is not None:
            self.__depth_first_traversal(node.right)
        print(node.value)

    def depth_first_search(self, value):
        node = self.root
        if self.root is None:
            print("Empty binary tree. Value not found.")
        else:
            result = self.__depth_first_search(node, value)
            return result

    def __depth_first_search(self, node, value):
        isFound = False
        if node.left is not None and isFound == False:
            isFound = isFound or self.__depth_first_search(node.left, value)
        if node.right is not None and isFound == False:
            isFound = isFound or self.__depth_first_search(node.right, value)
        if node.value == value:
            isFound = True

        return isFound

    def breadth_first_traversal(self):
        node = self.root
        if node is None:
            print("Empty binary tree.")
        else:
            self.__breadth_first_traversal(node)

    def __breadth_first_traversal(self, node):
        pass  # TODO

    def breadth_first_search(self, value):
        node = self.root
        if node is None:
            print("Empty binary tree. Value not found.")
        else:
            result = self.__breadth_first_search(node, value)
            return result

    def __breadth_first_search(self, node, value):
        pass # TODO

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