# coding=utf-8
"""
Python Specific Data Structures: List, Tuple, Dictionary

These data structures are specific to python language, and they give greater
flexibility in storing different types of data and faster processing in python
environment.

List − It is similar to array with the exception that the data elements
can be of different data types. You can have both numeric and string data
in a python list.

https://www.tutorialspoint.com/python_data_structure/python_lists_data_structure.htm
"""


def main():
    """
Accessing Values

To access values in lists, use the square brackets for slicing along with
the index or indices to obtain value available at that index.

    :return:
    """
    list1 = ['physics', 'chemistry', 1997, 2000]
    list2 = [1, 2, 3, 4, 5]

    print("list1[0]: ", list1[0])  # physics
    print("list2[1:5)]: ", list2[1:5])  # [2, 3, 4, 5]


if __name__ == '__main__':
    main()
