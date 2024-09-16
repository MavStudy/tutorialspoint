# coding=utf-8
"""
Python - Divide and Conquer

This program is an example of divide-and-conquer programming approach where the
binary search is implemented using python.

https://www.tutorialspoint.com/python_data_structure/python_divide_and_conquer.htm


Binary Search implementation

In binary search we take a sorted list of elements and start looking for an
element at the middle of the list. If the search value matches with the middle
value in the list we complete the search. Otherwise we eleminate half of the
list of elements by choosing whether to procees with the right or left half of
the list depending on the value of the item searched.

This is possible as the list is sorted and it is much quicker than linear
search.Here we divide the given list and conquer by choosing the proper half of
the list. We repeat this approcah till we find the element or conclude about
it's absence in the list.
"""


def bsearch(list, val):
    list_size = len(list)
    idx0 = 0
    idxn = list_size - 1
    # Find the middle most value
    while idx0 <= idxn:
        midval = (idx0 + idxn) // 2
        if list[midval] == val:
            return midval
        # Compare the value the middle most value
        if val > list[midval]:
            idx0 = midval + 1
        else:
            idxn = midval - 1
        if idx0 > idxn:
            return None


def main():
    """
    Binary search in the list

    :return:
    """
    # Initialize the sorted list
    list = [2, 7, 19, 34, 53, 72]

    # Print the search result
    print(bsearch(list, 72))
    print(bsearch(list, 11))


if __name__ == '__main__':
    main()
"""
Output

When the above code is executed, it produces the following result −
5
None
"""
