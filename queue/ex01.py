# coding=utf-8
"""
Python-Queue

We are familiar with queue in our day to day life as we wait for a service. The
queue data structure aslo means the same where the data elements are arranged
in a queue. The uniqueness of queue lies in the way items are added and removed.
The items are allowed at on end but removed form the other end. So it is
a First-in-First out method.

A queue can be implemented using python list where we can use the insert() and
pop() methods to add and remove elements. Their is no insertion as data
elements are always added at the end of the queue.

https://www.tutorialspoint.com/python_data_structure/python_queue.htm

"""


def separator(col=30):
    print('-' * col)


class Queue:
    def __init__(self):
        self.queue = list()

    def addtoq(self, dataval):
        """
        Insert method to add element

        :param dataval:
        :return:
        """
        if dataval not in self.queue:
            self.queue.insert(0, dataval)
            return True
        return False

    def size(self):
        return len(self.queue)


def main():
    """
    Adding Elements

    In the below example we create a queue class where we implement the
    First-in-First-Out method. We use the in-built insert method for adding
    data elements.

    :return:
    """
    TheQueue = Queue()
    TheQueue.addtoq("Mon")
    TheQueue.addtoq("Tue")
    TheQueue.addtoq("Wed")
    print(TheQueue.size())  # 3


if __name__ == '__main__':
    main()
