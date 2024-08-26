# coding=utf-8
"""
Python-Dequeue

A double-ended queue, or deque, supports adding and removing elements from
either end. The more commonly used stacks and queues are degenerate forms of
deques, where the inputs and outputs are restricted to a single end.

https://www.tutorialspoint.com/python_data_structure/python_dequeue.htm

"""
import collections as co


def main():
    """
    Output

    When the above code is executed, it produces the following result −

    :return:
    """
    DoubleEnded = co.deque(["Mon", "Tue", "Wed"])
    DoubleEnded.append("Thu")

    print("Appended at right - ")
    print(DoubleEnded)

    DoubleEnded.appendleft("Sun")
    print("Appended at right at left is - ")
    print(DoubleEnded)

    DoubleEnded.pop()
    print("Deleting form right - ")
    print(DoubleEnded)

    DoubleEnded.popleft()
    print("Deleting from left - ")
    print(DoubleEnded)


if __name__ == '__main__':
    main()
