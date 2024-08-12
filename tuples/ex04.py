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
    Delete Tuple Elements

    Removing individual tuple elements is not possible. There is, of course,
    nothing wrong with putting together another tuple with the undesired
    elements discarded.

    To explicitly remove an entire tuple, just use the del statement.

    :return:
    """
    tup = ('physics', 'chemistry', 1997, 2000)
    print(tup)
    del tup
    print("After deleting tup: ")
    print(tup)  # Note − an exception raised, this is because after del tup
    # tuple does not exist anymore.


if __name__ == '__main__':
    main()
