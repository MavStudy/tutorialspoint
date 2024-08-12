# coding=utf-8
"""
Python-2-D Array

Two-dimensional array is an array within an array. It is an array of arrays.
In this type of array the position of an data element is referred by two
indices instead of one. So it represents a table with rows and columns of data.

In the below example of a two-dimensional array, observer that each array
element itself is also an array.

https://www.tutorialspoint.com/python_data_structure/python_2darray.htm
"""
import array as arr


def main():
    """
    Consider the example of recording temperatures 4 times a day, every day.
    Some times the recording instrument may be faulty, and we fail to record
    data. Such data for 4 days can be presented as a two dimensional array as
    below.


    Accessing Values

    The data elements in two dimesnional arrays can be accessed using two
    indices. One index referring to the main or parent array and another index
    referring to the position of the data element in the inner array. If we
    mention only one index then the entire inner array is printed for that
    index position.

    :return:
    """
    T = [[11, 12, 5, 2], [15, 6, 10], [10, 8, 12, 5], [12, 15, 8, 6]]
    # When the above code is executed, it produces the following result:
    print(T[0])  # [11, 12, 5, 2]
    print(T[1][2])  # 10
    print('-' * 20)

    # To print out the entire two-dimensional array we can use python for loop
    # as shown below. We use end of line to print out the values in different
    # rows.
    for r in T:
        for c in r:
            print(c, end=" ")
        print()


if __name__ == '__main__':
    main()
