import networkx as nx
import matplotlib.pyplot as plt
from collections import deque


class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, first_node, connection_cord):
        if first_node not in self.graph:
            self.graph[first_node] = []
        self.graph[first_node].append(connection_cord)

    def dfs(self, first_node):
        visited = set()
        self.dfs_util(first_node, visited)

    def dfs_util(self, first_node, visited):
        visited.add(first_node)
        print(first_node, end=' ')

        if first_node in self.graph:
            for neighbor in self.graph[first_node]:
                if neighbor not in visited:
                    self.dfs_util(neighbor, visited)

    def bfs(self, first_cord):
        visited = set()
        queue = deque([first_cord])

        while queue:
            curr_node = queue.popleft()
            if curr_node not in visited:
                print(curr_node, end=' ')
                visited.add(curr_node)

                if curr_node in self.graph:
                    for neighbor in self.graph[curr_node]:
                        if neighbor not in visited:
                            queue.append(neighbor)

    def transpose(self):
        transposed_graph = Graph()
        for connection_node  in self.graph:
            for first_node in self.graph[connection_node]:
                transposed_graph.add_edge(first_node, connection_node)
        return transposed_graph

    def kosaraju(self):
        stack = []
        visited = set()
        scc_list = []

        for first_node in self.graph:
            if first_node not in visited:
                self.kosaraju_util(first_node, visited, stack)
                stack.append(None)  # Mark the end of a component

        transposed_graph = self.transpose()
        visited = set()

        while stack:
            first_node = stack.pop()
            if first_node is not None and first_node not in visited:
                scc = []
                transposed_graph.kosaraju_util(first_node, visited, scc)
                scc_list.append(scc)

        return scc_list

    def kosaraju_util(self, first_node, visited, scc):
        visited.add(first_node)
        scc.append(first_node)

        if first_node in self.graph:
            for neighbor in self.graph[first_node]:
                if neighbor not in visited:
                    self.kosaraju_util(neighbor, visited, scc)

    def is_connected(self):
        visited = set()
        self.dfs_util(next(iter(self.graph)), visited)

        return len(visited) == len(self.graph)

    def display_graph(self):
        g = nx.DiGraph()
        for connection_node in self.graph:
            for first_node in self.graph[connection_node]:
                g.add_edge(connection_node, first_node)

        pos = nx.spring_layout(g)
        nx.draw(g, pos, with_labels=True)
        plt.show()


if __name__ == '__main__':
    g = Graph()
    g.add_edge('A', 'B')
    g.add_edge('B', 'C')
    g.add_edge('C', 'A')
    g.add_edge('B', 'D')
    g.add_edge('D', 'E')
    g.add_edge('E', 'F')
    g.add_edge('F', 'D')
    g.add_edge('G', 'E')
    g.add_edge('A', 'E')
    g.add_edge('A', 'G')

    g.dfs('A')
    print("\n^^^^^^^^DFS")

    g.bfs('A')
    print("\n^^^^^^^^BFS")

    print("Silnie spójne składowe:")
    korasaj = g.kosaraju()
    for component in korasaj:
        print(component)
    print("\n")

    print("Graf spojny:", g.is_connected())
    print("\n")

    g.display_graph()
