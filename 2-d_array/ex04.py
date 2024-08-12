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
    Deleting the Values

    We can delete the entire inner array or some specific data elements of the
    inner array by reassigning the values using the del() method with index.
    But in case you need to remove specific data elements in one of the inner
    arrays, then use the update process described above.

    :return:
    """
    T = [[11, 12, 5, 2], [15, 6, 10], [10, 8, 12, 5], [12, 15, 8, 6]]

    del T[3]

    for r in T:
        for c in r:
            print(c, end=" ")
        print()
    """
    Output:
    
    11 12 5 2
    15 6 10
    10 8 12 5
    """


if __name__ == '__main__':
    main()
