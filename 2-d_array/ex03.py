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
    Updating Values

    We can update the entire inner array or some specific data elements of
    the inner array by reassigning the values using the array index.

    :return:
    """
    T = [[11, 12, 5, 2], [15, 6, 10], [10, 8, 12, 5], [12, 15, 8, 6]]

    T[2] = [11, 9]
    T[0][3] = 7

    for r in T:
        for c in r:
            print(c, end=" ")
        print()
    """
    Output:
    
    11 12 5 7
    15 6 10
    11 9 
    12 15 8 6
    """


if __name__ == '__main__':
    main()
