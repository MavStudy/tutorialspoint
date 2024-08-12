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
    Accessing Values in Dictionary

    To access dictionary elements, you can use the familiar square brackets
    along with the key to obtain its value.

    :return:
    """
    dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
    print("dict['Name']: ", dict['Name'])  # dict['Name']:  Zara
    print("dict['Age']: ", dict['Age'])  # dict['Age']:  7

    # If we attempt to access a data item with a key, which is not part of the
    # dictionary, we get an error as follows
    print("dict['Alice']: ", dict['Alice'])  # KeyError: 'Alice'


if __name__ == '__main__':
    main()
