__author__ = 'Jeremy Turinetti'

class BinaryTree(object):
    def __init__(self, root_value=None):
        self.__height = 0
        self.__left_height = 0
        self.__right_height = 0

        if root_value is None:
            self.__root = None
            self.__size = 0
        else:
            assert isinstance(root_value, int)
            self.__root = _Node(root_value)
            self.__size = 1

    def __insert(self, node):
        assert isinstance(node, _Node)

        cur_node = self.__root
        done = False
        cur_height = 0

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

            cur_height += 1

        # increase tree height
        if cur_height > self.__height:
            self.__height = cur_height

        # increase tree size
        self.__size = self.__size + 1

    def insert(self, value):
        node = _Node(value)
        if self.__root is None:
            self.__root = node
        else:
            self.__insert(node)

    def balance_tree(self):
        pass # TODO

    def print_tree(self):
        node = self.__root
        print("height: ", self.__height)
        print("size: ", self.__size)
        if self.__root is None:
            print("Empty binary tree.")
        else:
            self.__print_tree(node)

    def __print_tree(self, node):
        node.print_node()
        if node.left is not None:
            self.__print_tree(node.left)
        if node.right is not None:
            self.__print_tree(node.right)

    def depth_first_traversal(self):
        node = self.__root
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

    def breadth_first_traversal(self):
        node = self.__root
        if self.__root is None:
            print("Empty binary tree.")
        else:
            node_queue = [node]
            while len(node_queue) > 0:
                cur_node = node_queue.pop(0)
                print(cur_node.value)
                if cur_node.left is not None:
                    node_queue.append(cur_node.left)
                if cur_node.right is not None:
                    node_queue.append(cur_node.right)

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

    def print_node(self):
        print(self.value)
