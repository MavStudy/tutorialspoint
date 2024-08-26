# coding=utf-8
"""
Python-Advanced Linked list

We have already seen Linked List in earlier chapter in which it is possible
only to travel forward. In this chapter we see another type of linked list in
which it is possible to travel both forward and backward. Such a linked list
is called Doubly Linked List. Following is the features of doubly linked list.

• Doubly Linked List contains a link element called first and last.

• Each link carries a data field(s) and two link fields called next and prev.

• Each link is linked with its next link using its next link.

• Each link is linked with its previous link using its previous link.

• The last link carries a link as null to mark the end of the list.

https://www.tutorialspoint.com/python_data_structure/python_advanced_linked_list.htm

"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class doubly_linked_list:
    def __init__(self):
        self.head = None

    def push(self, NewVal):
        """
        Adding data element

        :param NewVal:
        :return:
        """
        NewNode = Node(NewVal)
        NewNode.next = self.head
        if self.head is not None:
            self.head.prev = NewNode
        self.head = NewNode

    def listprint(self, node):
        """
        Print the Double Linked list

        :param node:
        :return:
        """
        while node is not None:
            print(node.data)
            last = node
            node = node.next

    def insert(self, prev_node, NewVal):
        """
        Define the insert method to insert the element

        :param prev_node:
        :param NewVal:
        :return:
        """
        if prev_node is None:
            return
        NewNode = Node(NewVal)
        NewNode.next = prev_node.next
        prev_node.next = NewNode
        NewNode.prev = prev_node
        if NewNode.next is not None:
            NewNode.next.prev = NewNode


def main():
    """
    Inserting into Doubly Linked List

    Here, we are going to see how to insert a node to the Doubly Link List
    using the following program. The program uses a method named insert which
    inserts the new node at the third position from the head of the doubly
    linked list.

    :return:
    """
    dllist = doubly_linked_list()
    dllist.push(12)
    dllist.push(8)
    dllist.push(62)
    dllist.insert(dllist.head.next, 13)
    dllist.listprint(dllist.head)  # 62 8 13 12


if __name__ == '__main__':
    main()
