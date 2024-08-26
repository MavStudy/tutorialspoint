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
    """Create the node class"""
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class doubly_linked_list:
    """Create the doubly linked list class"""
    def __init__(self):
        self.head = None

    def push(self, NewVal):
        """
        Define the push method to add elements at the begining

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
        Define the method to Print the Double Linked list

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

    def append(self, NewVal):
        """
        Define the append method to add elements at the end

        :param NewVal:
        :return:
        """
        NewNode = Node(NewVal)
        NewNode.next = None
        if self.head is None:
            NewNode.prev = None
            self.head = NewNode
            return
        last = self.head
        while last.next is not None:
            last = last.next
        last.next = NewNode
        NewNode.prev = last
        return



def main():
    """
    Appending to a Doubly linked list

    Appending to a doubly linked list will add the element at the end.

    :return:
    """
    dllist = doubly_linked_list()
    dllist.push(12)
    dllist.append(9)
    dllist.push(8)
    dllist.push(62)
    dllist.append(45)
    dllist.listprint(dllist.head)  # 62 8 12 9 45


if __name__ == '__main__':
    main()
