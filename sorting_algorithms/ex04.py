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


def shell_sort(unsorted_list):
    """
    Shell Sort involves sorting elements which are away from each other. We
    sort a large sublist of a given list and go on reducing the size of the
    list until all elements are sorted. The below program finds the gap by
    equating it to half of the length of the list size and then starts sorting
    all elements in it. Then we keep resetting the gap until the entire list is
    sorted.

    Сортировка Шелла является оптимизированным вариантом сортировки вставками.

    Оптимизация достигается путем сравнения не только соседних элементов, но
    и элементов на определенном расстоянии, которое в течении работы алгоритма
    уменьшается. На последней итерации это расстояние равно 1. После этого
    алгоритм становится обычным алгоритмом сортировки вставками, что гарантирует
    правильный результат сортировки.

    Но следует отметить один момент: к тому времени, когда это произойдет, наш
    массив будет почти отсортирован, поэтому итерации будут выполнятся очень
    быстро.

    :param unsorted_list:
    :return:
    """
    gap = len(unsorted_list) // 2
    while gap > 0:
        for i in range(gap, len(unsorted_list)):
            temp = unsorted_list[i]
            j = i

            # Sort the sub list for this gap
            while j >= gap and unsorted_list[j - gap] > temp:
                unsorted_list[j] = unsorted_list[j - gap]
                j = j - gap
                unsorted_list[j] = temp

        # Reduce the gap for the next
        gap = gap // 2

    return unsorted_list

def shell_sort2(unsorted_list):
    n = len(unsorted_list)
    k = int(math.log2(n))
    gap = 2**k - 1
    while gap > 0:
        for i in range(gap, n):
            temp = unsorted_list[i]
            j = i
            while j >= gap and unsorted_list[j - gap] > temp:
                unsorted_list[j] = unsorted_list[j - gap]
                j -= gap
            unsorted_list[j] = temp
        k -= 1
        gap = 2**k - 1
    return unsorted_list


def main():
    """

    :return:
    """
    unsorted_list = [19, 2, 31, 45, 30, 11, 121, 27]
    print(f"{unsorted_list = }")
    print(f"  sorted_list = {shell_sort(unsorted_list)}")
    print(f"  sorted_list = {shell_sort2(unsorted_list)}")


if __name__ == '__main__':
    main()
"""
Output

When the above code is executed, it produces the following result −

unsorted_list = [19, 2, 31, 45, 30, 11, 121, 27]
  sorted_list = [2, 11, 19, 27, 30, 31, 45, 121]
"""
