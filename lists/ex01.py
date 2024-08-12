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
    Creating a list is as simple as putting different comma-separated values
    between square brackets.

    :return:
    """
    list1 = ['physics', 'chemistry', 1997, 2000]
    list2 = [1, 2, 3, 4, 5]
    list3 = ["a", "b", "c", "d"]

    print(list1)
    print(list2)
    print(list3)


if __name__ == '__main__':
    main()
