# coding=utf-8
"""
Python - Recursion

Recursion is a fundamental programming concept where a function calls itself in
order to solve a problem. This technique breaks down a complex problem into
smaller and more manageable sub-problems of the same type. In Python, recursion
is implemented by defining a function that makes one or more calls to itself
within its own body.

https://www.tutorialspoint.com/python/python_recursion.htm

Binary Search using Recursion

Binary search is a powerful algorithm for quickly finding elements in sorted
lists, with logarithmic time complexity making it highly efficient.

Let us have a look at another example to understand how recursion works. The
problem at hand is to check whether a given number is present in a list.

While we can perform a sequential search for a certain number in the list using
a for loop and comparing each number, the sequential search is not efficient
especially if the list is too large. The binary search algorithm that checks if
the index 'high' is greater than index 'low. Based on value present at 'mid'
variable, the function is called again to search for the element.

We have a list of numbers, arranged in ascending order. We find the
midpoint of the list and restrict the checking to either left or right of
midpoint depending on whether the desired number is less than or greater than
the number at midpoint.

Example

The following code implements the recursive binary searching technique.
"""


def bsearch(my_list, low, high, elem):
    if high >= low:
        mid = (high + low) // 2
        if my_list[mid] == elem:
            return mid
        elif my_list[mid] > elem:
            return bsearch(my_list, low, mid - 1, elem)
        else:
            return bsearch(my_list, mid + 1, high, elem)
    else:
        return -1


def main():
    """
   Use recursive function to binary searching.

    :return:
    """
    my_list = [5, 12, 23, 45, 49, 67, 71, 77, 82]
    num = 67
    print("The list is")
    print(my_list)
    print("Check for number:", num)
    my_result = bsearch(my_list, 0, len(my_list) - 1, num)

    if my_result != -1:
        print("Element found at index", str(my_result))
    else:
        print("Element not found!")

if __name__ == '__main__':
    main()
"""
Output

The list is
[5, 12, 23, 45, 49, 67, 71, 77, 82]
Check for number: 67
Element found at index 5

"""
