from binarytree import BinaryTree
from random import randint
__author__ = 'Jeremy Turinetti'

def main():
    # test code here
    my_tree = BinaryTree()
    for iter in range(0, 100):
        num = randint(0, 1000)
        my_tree.insert_value(num)

    my_tree.print_tree()

main()