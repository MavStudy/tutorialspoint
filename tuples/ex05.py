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
    Basic Tuples Operations

    Tuples respond to the + and * operators much like strings; they mean
    concatenation and repetition here too, except that the result is a new
    tuple, not a string.

    In fact, tuples respond to all of the general sequence operations we used
    on strings in the prior chapter.

    :return:
    """
    print(len((1, 2, 3))) # 3 - Length

    print((1, 2, 3) + (4, 5, 6))  # (1, 2, 3, 4, 5, 6) - Concatenation

    print(('Hi!',) * 4)  # ('Hi!', 'Hi!', 'Hi!', 'Hi!') - Repetition

    print(3 in (1, 2, 3))  # True - Membership

    for x in (1, 2, 3):  # Iteration
        print(x)


if __name__ == '__main__':
    main()
