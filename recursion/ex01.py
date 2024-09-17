# coding=utf-8
"""
Python - Recursion

Recursion is a fundamental programming concept where a function calls itself in
order to solve a problem. This technique breaks down a complex problem into
smaller and more manageable sub-problems of the same type. In Python, recursion
is implemented by defining a function that makes one or more calls to itself
within its own body.

https://www.tutorialspoint.com/python/python_recursion.htm

Example

The following example shows hows you can use a recursive function to calculate
factorial.
"""


def factorial(n):
    if n == 1:
        print(n)
        return 1  # base case
    else:
        print(n, '*', end=' ')
        return n * factorial(n - 1)  # Recursive case



def main():
    """
   Use recursive function to calculate factorial.

    :return:
    """
    print('factorial of 5=', factorial(5))


if __name__ == '__main__':
    main()
"""
Output

The above programs generates the following output −
5 * 4 * 3 * 2 * 1
factorial of 5= 120
"""
