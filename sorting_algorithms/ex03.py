# coding=utf-8
"""
Python - Sorting Algorithms

Sorting refers to arranging data in a particular format. Sorting algorithm
specifies the way to arrange data in a particular order. Most common orders are
in numerical or lexicographical order.

The importance of sorting lies in the fact that data searching can be optimized
to a very high level, if data is stored in a sorted manner. Sorting is also
used to represent data in more readable formats. Below we see five such
implementations of sorting in python.

• Bubble Sort

• Mege Sort

• Insertion Sort

• Shell Sort

• Selection Sort

https://www.tutorialspoint.com/python_data_structure/python_sorting_algorithms.htm

https://pythonist.ru/sortirovka-vstavkami-na-python/?ysclid=m1eq8hv37v589260878

"""


def insertion_sort(unsorted_list):
    """
    Insertion sort involves finding the right place for a given element in
    a sorted list. So in beginning we compare the first two elements and sort
    them by comparing them. Then we pick the third element and find its proper
    position among the previous two sorted elements. This way we gradually go
    on adding more elements to the already sorted list by putting them in their
     proper position.

    Суть сортировки
        1. Перебираются элементы в неотсортированной части массива.
        2. Каждый элемент вставляется в отсортированную часть массива на то
           место, где он должен находиться.

    :param unsorted_list:
    :return:
    """
    for i in range(1, len(unsorted_list)):
        nxt_element = unsorted_list[i]
        j = i - 1
        # Compare the current element with next one
        while (nxt_element < unsorted_list[j]) and (j >= 0):
            unsorted_list[j + 1] = unsorted_list[j]
            j = j - 1
        unsorted_list[j + 1] = nxt_element

    return unsorted_list


def main():
    """

    :return:
    """
    unsorted_list = [19, 2, 31, 45, 30, 11, 121, 27]
    print(f"{unsorted_list = }")
    print(f"  sorted_list = {insertion_sort(unsorted_list)}")



if __name__ == '__main__':
    main()
"""
Output

When the above code is executed, it produces the following result −

unsorted_list = [19, 2, 31, 45, 30, 11, 121, 27]
  sorted_list = [2, 11, 19, 27, 30, 31, 45, 121]
"""
