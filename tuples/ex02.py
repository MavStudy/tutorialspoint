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
    Accessing Values in Tuples

    To access values in tuple, use the square brackets for slicing along with
    the index or indices to obtain value available at that index.

    :return:
    """
    tup1 = ('physics', 'chemistry', 1997, 2000)
    tup2 = (1, 2, 3, 4, 5, 6, 7)
    print("tup1[0]: ", tup1[0])  # physics
    print("tup2[1:5]: ", tup2[1:5])  # (2, 3, 4, 5)


if __name__ == '__main__':
    main()
