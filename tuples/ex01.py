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
    Creating a tup is as simple as putting different comma-separated values
    between square brackets.

    :return:
    """
    tup1 = ('physics', 'chemistry', 1997, 2000)
    tup2 = (1, 2, 3, 4, 5)
    tup3 = ("a", "b", "c", "d")

    print(tup1)
    print(tup2)
    print(tup3)

    tup1 = ()  # The empty tuple is written as two parentheses containing
    # nothing
    print(tup1)

    tup1 = (50, )  # To write a tuple containing a single value you have
    # to include a comma, even though there is only one value
    print(tup1)


if __name__ == '__main__':
    main()
