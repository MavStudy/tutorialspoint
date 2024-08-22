# coding=utf-8
"""
Python - Linked Lists

A linked list is a sequence of data elements, which are connected together via
links. Each data element contains a connection to another data element in form
of a pointer. Python does not have linked lists in its standard library. We
implement the concept of linked lists using the concept of nodes as discussed
in the previous chapter.

We have already seen how we create a node class and how to traverse the
elements of a node. In this chapter we are going to study the types of linked
lists known as singly linked lists. In this type of data structure there is
only one link between any two data elements. We create such a list and create
additional methods to insert, update and remove elements from the list.

https://www.tutorialspoint.com/python_data_structure/python_linked_lists.htm
"""


def separator(col=30):
    print('-' * col)


class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None


class SLinkedList:
    def __init__(self):
        self.headval = None


def main():
    """
    Creation of Linked list

    A linked list is created by using the node class we studied in the last
    chapter. We create a Node object and create another class to use this ode
    object. We pass the appropriate values through the node object to point the
    to the next data elements. The below program creates the linked list with
    three data elements. In the next section we will see how to traverse the
    linked list.

    :return:
    """
    list1 = SLinkedList()
    list1.headval = Node("Mon")
    e2 = Node("Tue")
    e3 = Node("Wed")
    # Link first Node to second node
    list1.headval.nextval = e2

    # Link second Node to third node
    e2.nextval = e3

    print(f"list1 = {list1}")


if __name__ == '__main__':
    main()
