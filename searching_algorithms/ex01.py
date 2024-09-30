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

Linear Search

In this type of search, a sequential search is made over all items one by one.
Every item is checked and if a match is found then that particular item is
returned, otherwise the search continues till the end of the data structure.
"""


def linear_search(values, search_for):
    """
    Every item is checked and if a match is found then that particular item is
    returned, otherwise the search continues till the end of the data structure.

    :param values:
    :param search_for
    :return:
    """
    search_at = 0
    search_res = False
    # Match the value with each data element
    while search_at < len(values) and search_res is False:
        if values[search_at] == search_for:
            search_res = True
        else:
            search_at = search_at + 1
    return search_res

def main():
    """

    :return:
    """
    l = [64, 34, 25, 12, 22, 11, 90]
    print(linear_search(l, 12))
    print(linear_search(l, 91))


if __name__ == '__main__':
    main()
"""
Output

When the above code is executed, it produces the following result −

True
False
"""
