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

    def listprint(self):
        """
        Print the linked list
        :return:
        """
        printval = self.headval
        while printval is not None:
            print(printval.dataval)
            printval = printval.nextval

    def AtBegining(self, newdata):
        NewNode = Node(newdata)
        # Update the new nodes next val to existing node
        NewNode.nextval = self.headval
        self.headval = NewNode

    def AtEnd(self, newdata):
        NewNode = Node(newdata)
        if self.headval is None:  # если список пуст
            self.headval = NewNode
            return
        laste = self.headval
        while laste.nextval:
            laste = laste.nextval
        laste.nextval = NewNode

    def Inbetween(self, middle_node, newdata):
        if middle_node is None:
            print("The mentioned node is absent")
            return

        NewNode = Node(newdata)
        NewNode.nextval = middle_node.nextval
        middle_node.nextval = NewNode


def main():
    """
    Insertion  Linked List

    Inserting element in the linked list involves reassigning the pointers from
    the existing nodes to the newly inserted node. Depending on whether the new
    data element is getting inserted at the beginning or at the middle or at
    the end of the linked list, we have the below scenarios.

    Inserting in between two Data Nodes

    This involves changing the pointer of a specific node to point to the new
    node. That is possible by passing in both the new node and the existing node
    after which the new node will be inserted. So we define an additional class
    method which will change the next pointer of the new node to the next
    pointer of middle node. Then assign the new node to next pointer of
    the middle node.

    :return:
    """
    list = SLinkedList()
    list.headval = Node("Mon")
    e2 = Node("Tue")
    e3 = Node("Wed")
    # Link first Node to second Node
    list.headval.nextval = e2
    e2.nextval = e3

    list.listprint()
    separator()

    list.Inbetween(list.headval.nextval, "Fri")
    list.listprint()


if __name__ == '__main__':
    main()
