# coding=utf-8
"""
Python - Search Tree

A Binary Search Tree (BST) is a tree in which all the nodes follow the
below-mentioned properties.The left sub-tree of a node has a key less than or
equal to its parent node's key.The right sub-tree of a node has a key greater
than to its parent node's key.Thus, BST divides all its sub-trees into two
segments; the left sub-tree and the right sub-tree

left_subtree (keys)  ≤  node (key)  ≤  right_subtree (keys)

https://www.tutorialspoint.com/python_data_structure/python_binary_search_tree.htm

"""


class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        """
        Insert method to create nodes

        :param data:
        :return:
        """
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def findval(self, lkpval):
        """
        findval method to compare the value with nodes

        :param lkpval:
        :return:
        """
        if lkpval < self.data:
            if self.left is None:
                return str(lkpval) + " Not Found"
            return self.left.findval(lkpval)
        elif lkpval > self.data:
            if self.right is None:
                return str(lkpval) + " Not Found"
            return self.right.findval(lkpval)
        elif lkpval == self.data:
            # print(str(self.data) + ' is found')
            return str(self.data) + ' is found'

    def print_tree(self):
        """
        Print the tree

        :return:
        """
        if self.left:
            self.left.print_tree()
        print(self.data)
        if self.right:
            self.right.print_tree()


def main():
    """
    Example search for a value in a B-tree

    :return:
    """
    root = Node(12)
    root.insert(6)
    root.insert(14)
    root.insert(3)
    root.print_tree()
    print(root.findval(7))
    print(root.findval(14))


if __name__ == '__main__':
    main()
