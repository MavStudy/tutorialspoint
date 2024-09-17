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

Following is the example of the Recursive case. In this example we are
generating the Fibonacci sequence in which the recursive case sums the results
of the two preceding Fibonacci numbers

"""


def fibonacci(n):
    if n <= 0:
        return 0  # Base case for n = 0
    elif n == 1:
        return 1  # Base case for n = 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)  # Recursive case



def main():
    """
   Use recursive function to generate the Fibonacci sequence.

    :return:
    """
    fib_series = [fibonacci(i) for i in range(6)]
    print(fib_series)


if __name__ == '__main__':
    main()
"""
Output

The above programs generates the following output −
[0, 1, 1, 2, 3, 5]
"""
