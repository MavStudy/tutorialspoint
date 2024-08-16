# coding=utf-8
"""
Python - Sets

Mathematically a set is a collection of items not in any particular order.
A Python set is similar to this mathematical definition with below additional
conditions.

• The elements in the set cannot be duplicates.

• The elements in the set are immutable(cannot be modified) but the set as a
  whole is mutable.

• There is no index attached to any element in a python set. So they do not
  support any indexing or slicing operation.


Set Operations

The sets in python are typically used for mathematical operations like union,
intersection, difference and complement etc. We can create a set, access
it’s elements and carry out these mathematical operations as shown below.

https://www.tutorialspoint.com/python_data_structure/python_sets.htm
"""


def separator(col=30):
    print('-' * col)


def main():
    """
    Removing Item from a Set

    We can remove elements from a set by using discard() method. Again as
    discussed there is no specific index attached to the newly added element.

    :return:
    """
    separator(50)

    Days = set(["Mon", "Tue", "Wed", "Thu", "Fri", "Sat"])
    print(Days)
    separator(50)
    Days.discard("Mon")
    # Days.discard("Sun")
    print(Days)


if __name__ == '__main__':
    main()
