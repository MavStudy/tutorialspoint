# coding=utf-8
"""
Python - Backtracking

Backtracking is a form of recursion. But it involves choosing only option out
of any possibilities. We begin by choosing an option and backtrack from it,
if we reach a state where we conclude that this specific option does not give
the required solution. We repeat these steps by going across each available
option until we get the desired solution.

Below is an example of finding all possible order of arrangements of a given
set of letters. When we choose a pair we apply backtracking to verify if that
exact pair has already been created or not. If not already created, the pair
is added to the answer list else it is ignored.

Ниже приведен пример поиска всех возможных вариантов расположения букв
в заданном наборе. Когда мы выбираем пару, мы применяем обратный поиск,
чтобы проверить, была ли уже создана именно эта пара. Если пара еще не создана,
она добавляется в список ответов, в противном случае она игнорируется.

https://www.tutorialspoint.com/python_data_structure/python_backtracking.htm

"""


def permute(list, s):
    if list == 1:
        return s
    else:
        return [
            y + x
            for y in permute(1, s)
            for x in permute(list - 1, s)
        ]


def main():
    """
    Example of finding all possible order of arrangements of a given set of
    letters

    :return:
    """
    print(permute(1, ["a", "b", "c"]))
    print(permute(2, ["a", "b", "c"]))


if __name__ == '__main__':
    main()
"""
Output

When the above code is executed, it produces the following result −

['a', 'b', 'c']
['aa', 'ab', 'ac', 'ba', 'bb', 'bc', 'ca', 'cb', 'cc']
"""
