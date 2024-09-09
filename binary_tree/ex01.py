# coding=utf-8
"""
Python-Binary Tree

Tree represents the nodes connected by edges. It is a non-linear data
structure. It has the following properties

• One node is marked as Root node.

• Every node other than the root is associated with one parent node.

• Each node can have an arbiatry number of chid node.

We create a tree data structure in python by using the concept os node
discussed earlier. We designate one node as root node and then add more nodes
as child nodes. Below is program to create the root node.

https://www.tutorialspoint.com/python_data_structure/python_binary_tree.htm

"""


class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def PrintTree(self):
        print(self.data)


def main():

    """
    Create Root

    We just create a Node class and add assign a value to the node. This
    becomes tree with only a root node.

    :return:
    """
    root = Node(10)
    root.PrintTree()  # 10


if __name__ == '__main__':
    main()
