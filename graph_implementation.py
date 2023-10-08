class Node:
    def __init__(self, value=None, edge=None):
        self.value = value
        self.edge = edge


class Graph:

    def __init__(self):
        self.numberofnodes = 0
        self.adjacentlist = {}

    def add_vertex(self, node):
        self.adjacentlist[node] = []
        self.numberofnodes += 1

    def add_edge(self, node1, node2):
        self.adjacentlist[node1].append(node2)
        self.adjacentlist[node2].append(node1)
