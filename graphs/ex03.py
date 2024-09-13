# coding=utf-8
"""
Python - Graphs

A graph is a pictorial representation of a set of objects where some pairs of
objects are connected by links. The interconnected objects are represented by
points termed as vertices, and the links that connect the vertices are called
edges. The various terms and functionalities associated with a graph is
described in great detail in our tutorial here.

In this chapter we are going to see how to create a graph and add various data
elements to it using a python program. Following are the basic operations we
perform on graphs.

• Display graph vertices

• Display graph edges

• Add a vertex

• Add an edge

• Creating a graph

A graph can be easily presented using the python dictionary data types. We
represent the vertices as the keys of the dictionary and the connection between
the vertices also called edges as the values in the dictionary.

Take a llok at the following graph -

a  •----------•b
   |          |
   |          |
   |          |
   |          |
c  •----------•---------•e
              d

In the above graph,

V = {a, b, c d, e}
E = {ab, ac, bd, cd, de}

https://www.tutorialspoint.com/python_data_structure/python_graphs.htm

-------------------------------------------------------------------------------
Display graph vertices

To display the graph vertices we simple find the keys of the graph dictionary.
We use the keys() method.

-------------------------------------------------------------------------------
Display graph edges

Finding the graph edges is little tricker than the vertices as we have to find
each of the pairs of vertices which have an edge in between them. So we create
an empty list of edges then iterate through the edge values associated with
each of the vertices. A list is formed containing the distinct group of edges
found from the vertices.

"""


class graph:
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = []
        self.gdict = gdict

    # Get the keys of the dictionary
    def getVertices(self):
        return list(self.gdict.keys())

    def edges(self):
        return self.findedges()

    # Find the distinct list of edges
    def findedges(self):
        edgename = []
        for vrtx in self.gdict:
            for nxtvrtx in self.gdict[vrtx]:
                if {nxtvrtx, vrtx} not in edgename:
                    edgename.append({vrtx, nxtvrtx})
        return edgename


def main():
    """

    :return:
    """
    # We can present this graph in a python program as below -
    # create the dictionary with graph elements
    graph_elements = {
        "a": ["b", "c"],
        "b": ["a", "d"],
        "c": ["a", "d"],
        "d": ["e"],
        "e": ["d"]
    }
    # Print the graph
    print(graph_elements)
    # When the above code is executed, it produces the following result -
    # {'a': ['b', 'c'], 'b': ['a', 'd'], 'c': ['a', 'd'], 'd': ['e'],
    # 'e': ['d']}

    g = graph(graph_elements)
    print(g.getVertices())  # ['a', 'b', 'c', 'd', 'e']

    print(g.edges())


if __name__ == '__main__':
    main()
