__author__ = 'Jeremy Turinetti'

class BTree(object):
    def __init__(self, order):
        self.order = order
        self.root = _BTreeNode(order)

    def insert(self, value):
        node = self.root
        found = False

        while not found:
            largest_value = node.values[len(node.values) - 1]
            if len(node.values) < self.order:
                node.values.append(value)
                node.values.sort()
                found = True
            else:
                # need to check child nodes
                pass # TODO


class _BTreeNode(object):
    def __init__(self, order):
        self.order = order
        self.values = []
        self.children = []