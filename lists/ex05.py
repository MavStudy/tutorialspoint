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
    Basic List Operations

    Lists respond to the + and * operators much like strings; they mean
    concatenation and repetition here too, except that the result is a new
    list, not a string.

    In fact, lists respond to all of the general sequence operations we used
    on strings in the prior chapter.

    :return:
    """

    list1 = [1, 2, 3]
    print(len(list1))    # length: 3
    list2 = [1, 2, 3] + [4, 5, 6]
    print(list2)  # concatenation: [1, 2, 3, 4, 5, 6]
    list3 = ['Hi!'] * 4
    print(list3)  # repetition: ['Hi!', 'Hi!', 'Hi!', 'Hi!']
    print(3 in [1, 2, 3])  # membership: True
    for x in [1, 2, 3]:  # iteration: 1 2 3
        print(x, end=' ')


if __name__ == '__main__':
    main()
