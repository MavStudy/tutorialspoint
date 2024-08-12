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
    Delete List Elements

    To remove a list element, you can use either the del statement if you know
    exactly which element(s) you are deleting or the remove() method if you do
    not know.

    • Note − remove() method is discussed in subsequent section.

    :return:
    """

    list1 = ['physics', 'chemistry', 1997, 2000]
    print(list1)
    print(list1[2])  # ['physics', 'chemistry', 1997, 2000]
    del list1[2]
    print("After deleting value at index 2: ")  # after deleting
    # ['physics', 'chemistry', 2000]
    print(list1)


if __name__ == '__main__':
    main()
