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
Adding a vertex

Adding a vertex is straight forward where we add another additional key to the
graph dictionary.
-------------------------------------------------------------------------------
Adding an edge

Adding an edge to an existing graph involves treating the new vertex as a tuple
and validating if the edge is already present. If not then the edge is added.

"""


class graph:
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = {}
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

    # Add the vertex as a key
    def addVertex(self, vrtx):
        if vrtx not in self.gdict:
            self.gdict[vrtx] = []

    # Add the new edge
    def addEdge(self, edge):
        edge = set(edge)
        (vrtx1, vrtx2) = tuple(edge)
        if vrtx1 in self.gdict:
            self.gdict[vrtx1].append(vrtx2)
        else:
            self.gdict[vrtx1] = [vrtx2]



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

    print(g.edges())  # [{'b', 'a'}, {'c', 'a'}, {'d', 'b'}, {'d', 'c'},
    # {'d', 'e'}]

    g.addEdge({'a', 'e'})
    g.addEdge({'a', 'c'})
    print(g.edges())  # [{'b', 'a'}, {'c', 'a'}, {'d', 'b'}, {'d', 'c'},
    # {'d', 'e'}, {'e', 'a'}]


if __name__ == '__main__':
    main()
