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

https://pythonist.ru/algoritmy-sortirovki-s-python/

"""
import math


def selection_sort(input_list):
    """
    In selection sort we start by finding the minimum value in a given list
    and move it to a sorted list. Then we repeat the process for each of the
    remaining elements in the unsorted list. The next element entering the
    sorted list is compared with the existing elements and placed at its
    correct position.So, at the end all the elements from the unsorted list are
    sorted.
    При сортировке по выбору мы начинаем с поиска минимального значения в
    заданном списке и перемещаем его в отсортированный список. Затем мы
    повторяем процесс для каждого из оставшихся элементов в несортированном
    списке. Следующий элемент, входящий в отсортированный список, сравнивается
    с существующими элементами и помещается в правильное положение. Итак,
    в конце все элементы из несортированного списка сортируются.

    :param unsorted_list:
    :return:
    """
    for idx in range(len(input_list)):
        min_idx = idx
        for j in range(idx + 1, len(input_list)):
            if input_list[min_idx] > input_list[j]:
                min_idx = j
        # Swap the minimum value with the compared value
        input_list[idx], input_list[min_idx] = input_list[min_idx], \
                                               input_list[idx]


def main():
    """

    :return:
    """
    l = [19, 2, 31, 45, 30, 11, 121, 27]
    print(f"unsorted {l = }")
    selection_sort(l)
    print(f"  sorted {l = }")


if __name__ == '__main__':
    main()
"""
Output

When the above code is executed, it produces the following result −

unsorted l = [19, 2, 31, 45, 30, 11, 121, 27]
  sorted l = [2, 11, 19, 27, 30, 31, 45, 121]
"""
