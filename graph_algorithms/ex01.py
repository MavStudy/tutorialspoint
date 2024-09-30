# coding=utf-8
"""
Python - Graph Algorithms

Graphs are very useful data structures in solving many important mathematical
challenges. For example computer network topology or analysing molecular
structures of chemical compounds. They are also used in city traffic or route
planning and even in human languages and their grammar. All these applications
have a common challenge of traversing the graph using their edges and ensuring
that all nodes of the graphs are visited. There are two common established
methods to do this traversal which is described below.
Графики - это очень полезные структуры данных для решения многих важных
математических задач. Например, для топологии компьютерных сетей или анализа
молекулярных структур химических соединений. Они также используются при
планировании городского движения или маршрутов и даже в человеческих языках
и их грамматике. Все эти приложения имеют общую задачу обхода графа
с использованием своих ребер и обеспечения того, чтобы были посещены все узлы
графа. Существует два общепринятых метода обхода, которые описаны ниже.

https://www.tutorialspoint.com/python_data_structure/python_graph_algorithms.htm

Depth First Traversal

Also called depth first search (DFS),this algorithm traverses a graph in a
depth ward motion and uses a stack to remember to get the next vertex to start
a search, when a dead end occurs in any iteration. We implement DFS for a graph
in python using the set data types as they provide the required functionalities
to keep track of visited and unvisited nodes.
Также называемый поиском в глубину (DFS), этот алгоритм обходит граф в движении
в глубину и использует стек, чтобы запомнить, как получить следующую вершину
для начала поиска, когда на любой итерации возникает тупик. Мы реализуем DFS
для графа на python, используя заданные типы данных, поскольку они предоставляют
необходимые функциональные возможности для отслеживания посещенных и
непосещенных узлов.
"""


class graph:
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = {}
            self.gdict = gdict


def dfs(graph, start, visited=None):
    """
    Check for the visited and unvisited nodes

    :param graph:
    :param start:
    :param visited:
    :return:
    """
    if visited is None:
        visited = set()
    visited.add(start)
    print(start)
    for _next in graph[start] - visited:
        dfs(graph, _next, visited)
    return visited


def main():
    """

    :return:
    """
    gdict = {
        "a": set(["b", "c"]),
        "b": set(["a", "d"]),
        "c": set(["a", "d"]),
        "d": set(["e"]),
        "e": set(["a"])
    }
    dfs(gdict, 'a')


if __name__ == '__main__':
    main()
"""
Output

When the above code is executed, it produces the following result −

a
b
d
e
c
"""
