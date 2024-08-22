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

    def RemoveNode(self, Removekey):
        HeadVal = self.headval

        if HeadVal is not None:
            if HeadVal.dataval == Removekey:  # Если удаляемый элемент 1-й
                self.headval = HeadVal.nextval
                HeadVal = None
                return

            while HeadVal is not None:
                if HeadVal.dataval == Removekey:
                    break
                prev = HeadVal
                HeadVal = HeadVal.nextval

            if HeadVal == None:  # Если элемент не найден, то нечего удалять
                return

            prev.nextval = HeadVal.nextval
            HeadVal = None






def main():
    """
    Removing an Item

    We can remove an existing node using the key for that node. In the below
    program we locate the previous node of the node which is to be deleted.
    Then, point the next pointer of this node to the next node of the node to
    be deleted.

    :return:
    """
    list = SLinkedList()
    list.AtBegining("Mon")
    list.AtBegining("Tue")
    list.AtBegining("Wed")
    list.AtBegining("Thu")

    list.listprint()
    separator()

    list.RemoveNode("Tue")
    list.listprint()


if __name__ == '__main__':
    main()
