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
    Accessing Values in a Set

    We cannot access individual values in a set. We can only access all the
    elements together as shown above. But we can also get a list of individual
    elements by looping through the set.

    :return:
    """
    separator()

    Days = set(["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"])
    for d in Days:
        print(d)


if __name__ == '__main__':
    main()
