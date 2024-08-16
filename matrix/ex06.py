# coding=utf-8
"""
Python - Matrix

Matrix is a special case of two-dimensional array where each data element is
of strictly same size. So every matrix is also a two-dimensional array but
not vice versa.

Matrices are very important data structures for many mathematical and
scientific calculations. As we have already discussed two dimnsional array data
structure in the previous chapter we will be focusing on data structure
operations specific to matrices in this chapter.

We also be using the numpy package for matrix data manipulation.

https://www.tutorialspoint.com/python_data_structure/python_matrix.htm
"""
import numpy as np


def separator(col=30):
    print('-' * col)


def main():
    """
    Delete a column

    We can delete a column from a matrix using the delete() method. We have
    to specify the index of the column and also the axis value which is 0 for
    a row and 1 for a column.

    :return:
    """
    separator()
    m = np.array([
        ['Mon', 18, 20, 22, 17],
        ['Tue', 11, 18, 21, 18],
        ['Wed', 15, 21, 20, 19],
        ['Thu', 11, 20, 22, 21],
        ['Fri', 18, 17, 23, 22],
        ['Sat', 12, 22, 20, 18],
        ['Sun', 13, 15, 19, 16]
    ])
    print(f"{type(m)}\n{m}")
    separator()

    m = np.delete(m, [2], 1)
    print(m)


if __name__ == '__main__':
    main()
