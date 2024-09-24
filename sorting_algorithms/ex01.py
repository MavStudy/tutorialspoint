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

"""


def bubblesort(list):
    """
    Buble Sort is comparison-based algorithm in which each pair of adjacent
    elements is compared and the elements are swapped if they are not in order.

    :param list:
    :return:
    """
    # Swap the elements to arrange in order
    for iter_num in range(len(list) - 1, 0, -1):
        for idx in range(iter_num):
            if list[idx] > list[idx + 1]:
                temp = list[idx]
                list[idx] = list[idx + 1]
                list[idx + 1] = temp


def main():
    """

    :return:
    """
    list = [19, 2, 31, 45, 6, 11, 121, 27]
    bubblesort(list)
    print(list)


if __name__ == '__main__':
    main()
"""
Output

When the above code is executed, it produces the following result −

[2, 6, 11, 19, 27, 31, 45, 121]
"""
