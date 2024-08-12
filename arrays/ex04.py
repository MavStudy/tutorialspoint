# coding=utf-8
"""
Array − It is a sequential arrangement of data elements paired with the index
of the data element.
(Массив − это последовательное расположение элементов данных в паре с индексом
элемента данных)

Array is a container which can hold a fix number of items and these items
should be of the same type. Most of the data structures make use of arrays to
implement their algorithms. Following are the important terms to understand
the concept of Array are as follows −

• Element − Each item stored in an array is called an element.

• Index − Each location of an element in an array has a numerical index, which
  is used to identify the element.

https://www.tutorialspoint.com/python_data_structure/python_arrays.htm
"""
import array as arr


def main():
    """
    Deletion Operation

    Deletion refers to removing an existing element from the array
    and re-organizing all elements of an array.

    :return:
    """
    array1 = arr.array('i', [10, 20, 30, 40, 50])

    array1.remove(40)

    for x in array1:
        print(x)


if __name__ == '__main__':
    main()
