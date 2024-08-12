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
    Updating Lists

    You can update single or multiple elements of lists by giving the slice
    on the left-hand side of the assignment operator, and you can add
    to elements in a list with the append() method.

    • Note − append() method is discussed in subsequent section.

    :return:
    """

    list = ['physics', 'chemistry', 1997, 2000]
    print("Value available at index 2: ")
    print(list[2])  # 1997
    list[2] = 2001
    print("New value available at index 2: ")
    print(list[2])  # 2001


if __name__ == '__main__':
    main()
