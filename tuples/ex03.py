# coding=utf-8
"""
Python Specific Data Structures: List, Tuple, Dictionary

These data structures are specific to python language, and they give greater
flexibility in storing different types of data and faster processing in python
environment.

Tuple − Tuples are similar to tups but they are immutable which means the
values in a tuple cannot be modified they can only be read.

A tuple is a sequence of immutable Python objects. Tuples are sequences, just
like tups. The differences between tuples and lists are, the tuples cannot
be changed unlike tups and tuples use parentheses, whereas lists use square
brackets.

Creating a tuple is as simple as putting different comma-separated values.
Optionally you can put these comma-separated values between parentheses also.

https://www.tutorialspoint.com/python_data_structure/python_tuples_data_structure.htm
"""


def main():
    """
    Updating Tuples

    Tuples are immutable which means you cannot update or change the values
    of tuple elements. You are able to take portions of existing tuples to
    create new tuples as the following example demonstrates

    :return:
    """
    tup1 = (12, 34.56)
    tup2 = ('abc', 'xyz')

    # Following action is not valid for tuples
    # tup1[0] = 100

    # So let's create a new tuple as follows
    tup3 = tup1 + tup2
    print(tup3)  # (12, 34.56, 'abc', 'xyz')

if __name__ == '__main__':
    main()
