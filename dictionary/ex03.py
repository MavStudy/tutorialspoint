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
    Delete Dictionary Elements

    You can either remove individual dictionary elements or clear the entire
    contents of a dictionary. You can also delete entire dictionary in a single
    operation.

    :return:
    """
    dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
    print(dict)  # {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
    del dict['Name']  # remove entry with key 'Name'
    print(dict)  # {'Age': 7, 'Class': 'First'}

    dict.clear()  # remove all entries in dict
    print(dict)  # {}

    del dict  # delete entire dictionary

    # print("dict['Age']: ", dict['Age'])  # KeyError: 'Age'
    print("dict['School']: ", dict['School'])  # KeyError: 'School'





if __name__ == '__main__':
    main()
