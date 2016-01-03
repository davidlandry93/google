#!/usr/bin/env python

import unittest


class Graph:

    def __init__(self, n_nodes):
        self.adj_matrix = []

        for i in range(n_nodes):
            new_row = []
            for j in range(n_nodes):
                new_row.append(0)
            self.adj_matrix.append(new_row)

    def add_edge(self, node_from, node_to, cost):
        self.adj_matrix[node_from][node_to] = cost

    def cost(self, node_from, node_to):
        return self.adj_matrix[node_from][node_to]

    def neighbors(self, node):
        return filter(lambda x: self.adj_matrix[node][x] is not 0,
                      range(len(self)))

    def distance(self, from_node, to_node):
        return self.adj_matrix[from_node][to_node]

    def __len__(self):
        return len(self.adj_matrix)


class Dijkstra:

    def __init__(self, graph):
        self.graph = graph
        self.parents = [None] * len(graph)
        self.distances = [float('inf')] * len(graph)
        self.nodes = range(len(graph))

    def done(self):
        return len(self.nodes) is 0

    def compute(self):
        while not self.done():
            current_node = self.closest_unvisited_node()
            self.nodes.remove(current_node)

            for neighbor in self.unvisited_neighbors(current_node):
                new_distance = (self.distances[current_node] +
                                self.graph.distance(current_node, neighbor))
                if new_distance < self.distances[neighbor]:
                    self.parents[neighbor] = current_node
                    self.distances[neighbor] = new_distance

    def closest_unvisited_node(self):
        distances_of_unvisited = map(lambda x: self.distances[x], self.nodes)
        distance_of_closest = min(distances_of_unvisited)
        return self.nodes[distances_of_unvisited.index(distance_of_closest)]

    def unvisited_neighbors(self, node):
        set_of_nodes = set(self.nodes)
        return set_of_nodes.intersection(self.graph.neighbors(node))

    def shortest_path_to(self, node):
        path = []
        current_node = node
        while current_node is not self.start:
            path.append(self.parents[current_node])
            current_node = self.parents[current_node]

        return list(reversed(path))

    @classmethod
    def solve_graph(cls, graph, start):
        dijkstra = Dijkstra(graph)
        dijkstra.set_start(start)
        dijkstra.distances.sort()

        dijkstra.compute()

        return dijkstra

    def set_start(self, start):
        self.start = start
        self.distances[start] = 0


class TestGraph(unittest.TestCase):

    def setUp(self):
        self.graph = Graph(10)

    def test_add_edge(self):
        self.graph.add_edge(2, 5, 12)

        self.assertEqual(12, self.graph.cost(2, 5))

    def test_neighbors(self):
        self.graph.add_edge(2, 3, 1)
        self.graph.add_edge(2, 4, 1)

        self.assertEqual([3, 4], self.graph.neighbors(2))


class TestDijkstra(unittest.TestCase):

    def setUp(self):
        self.graph = Graph(10)
        self.graph.add_edge(0, 1, 12)
        self.graph.add_edge(0, 2, 4)
        self.graph.add_edge(1, 3, 1)
        self.graph.add_edge(2, 3, 10)
        self.graph.add_edge(2, 4, 2)

    def test_shortest_path(self):
        dijkstra_result = Dijkstra.solve_graph(self.graph, 0)

        self.assertEqual([0, 1], dijkstra_result.shortest_path_to(3))
        self.assertEqual([0, 2], dijkstra_result.shortest_path_to(4))

if __name__ == '__main__':
    unittest.main()
