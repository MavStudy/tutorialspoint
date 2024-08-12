# coding=utf-8
"""
Python Specific Data Structures: List, Tuple, Dictionary

These data structures are specific to python language, and they give greater
flexibility in storing different types of data and faster processing in python
environment.

Dictionary − The dictionary contains Key-value pairs as its data elements.

In Dictionary each key is separated from its value by a colon (:), the items
are separated by commas, and the whole thing is enclosed in curly braces. An
empty dictionary without any items is written with just two curly braces, like
this − {}.

Keys are unique within a dictionary while values may not be. The values of
a dictionary can be of any type, but the keys must be of an immutable data type
such as strings, numbers, or tuples.

https://www.tutorialspoint.com/python_data_structure/python_dictionary_data_structure.htm
"""


def main():
    """
    Properties of Dictionary Keys

    Dictionary values have no restrictions. They can be any arbitrary Python
    object, either standard objects or user-defined objects. However, same is
    not true for the keys.

    There are two important points to remember about dictionary keys

    • More than one entry per key not allowed. Which means no duplicate key is
    allowed. When duplicate keys encountered during assignment, the last
    assignment wins.

    :return:
    """
    dict = {'Name': 'Zara', 'Age': 7, 'Name': 'Manni'}
    print("dict['Name']: ", dict['Name'])  # dict['Name']: Manni

    # Keys must be immutable. Which means you can use strings, numbers or
    # tuples as dictionary keys but something like ['key'] is not allowed.
    dict = {['Name']: 'Zara', 'Age': 7}
    print("dict['Name']: ", dict['Name'])  # TypeError: unhashable type: 'list'


if __name__ == '__main__':
    main()
