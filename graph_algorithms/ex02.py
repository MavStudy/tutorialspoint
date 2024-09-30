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

Breadth First Traversal

Also called breadth first search (BFS),this algorithm traverses a graph
breadth ward motion and uses a queue to remember to get the next vertex to
start a search, when a dead end occurs in any iteration. Please visit this link
in our website to understand the details of BFS steps for a graph.
Также называемый поиском сначала в ширину (BFS), этот алгоритм обходит движение
графа в ширину и использует очередь, чтобы не забыть получить следующую вершину
для начала поиска, когда на любой итерации возникает тупик. Пожалуйста,
перейдите по этой ссылке на нашем веб-сайте, чтобы ознакомиться с подробностями
шагов BFS для построения графика.

We implement BFS for a graph in python using queue data structure discussed
earlier. When we keep visiting the adjacent unvisited nodes and keep adding it
to the queue. Then we start dequeue only the node which is left with no
unvisited nodes. We stop the program when there is no next adjacent node to be
visited.
Мы реализуем BFS для графа на python, используя структуру данных очереди,
рассмотренную ранее. Когда мы продолжаем посещать соседние непросмотренные
узлы и добавляем их в очередь. Затем мы начинаем выводить из очереди только тот
узел, в котором не осталось непросмотренных узлов. Мы останавливаем программу,
когда нет следующего соседнего узла, который нужно посетить.

"""
import collections


class graph:
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = {}
            self.gdict = gdict


def bfs(graph, startnode):
    """
    Track the visited and unvisited nodes using queue

    :param graph:
    :param startnode:
    :return:
    """
    seen, queue = set([startnode]), collections.deque([startnode])
    while queue:
        vertex = queue.popleft()  # vertex - вершина
        marked(vertex)
        for node in graph[vertex]:
            if node not in seen:
                seen.add(node)
                queue.append(node)


def marked(n):
    print(n)


def main():
    """

    :return:
    """
    # The graph dictionary
    gdict = {
        "a": set(["b", "c"]),
        "b": set(["a", "d"]),
        "c": set(["a", "d"]),
        "d": set(["e"]),
        "e": set(["a"])
    }
    bfs(gdict, 'a')


if __name__ == '__main__':
    main()
"""
Output

When the above code is executed, it produces the following result −

a
b
c
d
e
"""
