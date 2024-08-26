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

    def removeformq(self):
        """
        Pop method to remove element

        :return:
        """
        if self.size() > 0:
            return self.queue.pop()
        return "No elements in Queue!"


def main():
    """
    Removing Element

    In the below example we create a queue class where we insert the data and
    then remove the data using the in-built pop method.

    :return:
    """
    TheQueue = Queue()
    TheQueue.addtoq("Mon")
    TheQueue.addtoq("Tue")
    TheQueue.addtoq("Wed")
    print(TheQueue.removeformq())  # Mon
    print(TheQueue.removeformq())  # Tue


if __name__ == '__main__':
    main()
