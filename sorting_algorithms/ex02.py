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


def merge_sort(unsorted_list):
    """
    Merge sort first divides the array into equal halves and then combines them
    in a sorted manner.

    :param list:
    :return:
    """
    if len(unsorted_list) <= 1:
        return unsorted_list
    # Find the middle point and divide it
    middle = len(unsorted_list) // 2
    left_list = unsorted_list[:middle]
    right_list = unsorted_list[middle:]

    left_list = merge_sort(left_list)
    right_list = merge_sort(right_list)
    return list(merge(left_list, right_list))


def merge(left_half, right_half):
    """
    Merge the sorted halves

    :param left_half:
    :param right_half:
    :return:
    """
    res = []
    while len(left_half) != 0 and len(right_half) != 0:
        if left_half[0] < right_half[0]:
            res.append(left_half[0])
            left_half.remove(left_half[0])
        else:
            res.append(right_half[0])
            right_half.remove(right_half[0])

    if len(left_half) == 0:
        res = res + right_half
    else:
        res = res + left_half

    return res


def main():
    """

    :return:
    """
    unsorted_list = [64, 34, 25, 12, 22, 11, 90]
    print(merge_sort(unsorted_list))


if __name__ == '__main__':
    main()
"""
Output

When the above code is executed, it produces the following result −

[11, 12, 22, 25, 34, 64, 90]
"""
