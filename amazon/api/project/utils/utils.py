from collections import defaultdict
from amazon.api.project.utils import Table


class Graph(Table):
    def __init__(self):
        Table.__init__(self)
        self.nodes = set()
        self.edges = defaultdict(list)
        self.distances = {}
        self.__start_nodes_with_table()

    def __add_node(self, value):
        self.nodes.add(value)

    def __add_edge(self, from_node, to_node, distance):
        self.edges[from_node].append(to_node)
        self.distances[(from_node, to_node)] = distance

    def __start_nodes_with_table(self):
        new_nodes = self.table_positions()
        for new_node in new_nodes:
            self.__add_node(new_node)

        for from_node in self.nodes:
            for to_node in self.nodes:
                if to_node in self.weights[from_node]:
                    edge = self.weights[from_node][to_node]
                    self.__add_edge(from_node, to_node, edge)

    def dijkstra(self, initial, end):
        distances = {node: float("infinity") for node in self.nodes}
        distances[initial] = 0

        shortest_path = {}
        unvisited_nodes = set(self.nodes)

        while unvisited_nodes:
            current_node = min(unvisited_nodes, key=lambda node: distances[node])
            unvisited_nodes.remove(current_node)
            if current_node == end:
                break

            for neighbor in self.edges[current_node]:
                new_distance = (
                    distances[current_node] + self.distances[(current_node, neighbor)]
                )
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    shortest_path[neighbor] = current_node

        path = []
        current_node = end
        while current_node != initial:
            path.insert(0, current_node)
            current_node = shortest_path[current_node]
        path.insert(0, initial)

        return path, distances[end]
