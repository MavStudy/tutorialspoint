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
    Difference of Sets

    The difference operation on two sets produces a new set containing only the
    elements from the first set and none from the second set. In the below
    example the element “Wed” is present in both the sets so it will not be
    found in the result set.

    :return:
    """
    separator(50)
    DaysA = set(["Mon", "Tue", "Wed"])
    DaysB = set(["Wed", "Thu", "Fri", "Sat", "Sun"])
    print(DaysA)
    separator(50)
    print(DaysB)
    separator(50)
    AllDays = DaysA - DaysB
    print(AllDays)


if __name__ == '__main__':
    main()
