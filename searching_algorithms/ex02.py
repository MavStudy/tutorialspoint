# coding=utf-8
"""
Python - Searching Algorithms

Searching is a very basic necessity when you store data in different data
structures. The simplest approach is to go across every element in the data
structure and match it with the value you are searching for.This is known as
Linear search. It is inefficient and rarely used, but creating a program for
it gives an idea about how we can implement some advanced search algorithms.

Поиск является основной необходимостью, когда вы храните данные в различных
структурах данных. Самый простой подход заключается в том, чтобы просмотреть
каждый элемент структуры данных и сопоставить его с искомым значением. Это
называется линейным поиском. Он неэффективен и редко используется, но создание
программы для него дает представление о том, как мы можем реализовать некоторые
продвинутые алгоритмы поиска.

https://www.tutorialspoint.com/python_data_structure/python_searching_algorithms.htm

Interpolation Search

This search algorithm works on the probing position of the required value. For
this algorithm to work properly, the data collection should be in a sorted form
and equally distributed.Initially, the probe position is the position of the
middle most item of the collection.If a match occurs, then the index of the
item is returned.If the middle item is greater than the item, then the probe
position is again calculated in the sub-array to the right of the middle item.
Otherwise, the item is searched in the subarray to the left of the middle item.
This process continues on the sub-array as well until the size of subarray
reduces to zero.
"""


def intpolsearch(values, x):
    """
    There is a specific formula to calculate the middle position which is
    indicated in the program below.
    Существует специальная формула для расчета среднего положения, которая
    указана в программе ниже.

    :param values:
    :param x:
    :return:

    """
    idx0 = 0
    idxn = len(values) - 1
    while idx0 <= idxn and x >= values[idx0] and x <= values[idxn]:
        # Find the mid point
        mid = idx0 + int(((float(idxn - idx0) / (values[idxn] - values[idx0]))
                          * (x - values[idx0])))
        # Compare the value at mid point with search value
        if values[mid] == x:
            return "Found " + str(x) + " at index " + str(mid)
        if values[mid] < x:
            idx0 = mid + 1

    return "Searched element not in the list"


def main():
    """

    :return:
    """
    l = [2, 6, 11, 19, 27, 31, 45, 121]
    print(intpolsearch(l, 2))
    print(intpolsearch(l, 31))


if __name__ == '__main__':
    main()
"""
Output

When the above code is executed, it produces the following result −

True
False
"""
