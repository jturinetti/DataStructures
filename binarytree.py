__author__ = 'Jeremy Turinetti'

class BinaryTree(object):
    def __init__(self, root):
        assert isinstance(root, _Node)
        self.root = root

    def insert_node(self, node):
        assert isinstance(node, _Node)
        pass

    def insert_value(self, value):
        node = _Node(value)
        self.insert_node(self, node)

class _Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
