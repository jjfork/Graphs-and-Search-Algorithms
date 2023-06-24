import networkx as nx
import matplotlib.pyplot as plt
from collections import deque


class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, first_cord, connection_cord):
        if first_cord not in self.graph:
            self.graph[first_cord] = []
        self.graph[first_cord].append(connection_cord)

    def dfs(self, first_cord):
        visited = set()
        self.dfs_util(first_cord, visited)

    def dfs_util(self, first_cord, visited):
        visited.add(first_cord)
        print(first_cord, end=' ')

        if first_cord in self.graph:
            for neighbor in self.graph[first_cord]:
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
        for connection_cord in self.graph:
            for first_cord in self.graph[connection_cord]:
                transposed_graph.add_edge(first_cord, connection_cord)
        return transposed_graph

    def kosaraju(self):
        stack = []
        visited = set()
        scc_list = []

        for first_cord in self.graph:
            if first_cord not in visited:
                self.kosaraju_util(first_cord, visited, stack)
                stack.append(None)  # Mark the end of a component

        transposed_graph = self.transpose()
        visited = set()

        while stack:
            first_cord = stack.pop()
            if first_cord is not None and first_cord not in visited:
                scc = []
                transposed_graph.kosaraju_util(first_cord, visited, scc)
                scc_list.append(scc)

        return scc_list

    def kosaraju_util(self, first_cord, visited, scc):
        visited.add(first_cord)
        scc.append(first_cord)

        if first_cord in self.graph:
            for neighbor in self.graph[first_cord]:
                if neighbor not in visited:
                    self.kosaraju_util(neighbor, visited, scc)

    def is_connected(self):
        visited = set()
        self.dfs_util(next(iter(self.graph)), visited)

        return len(visited) == len(self.graph)

    def display_graph(self):
        g = nx.DiGraph()
        for connection_cord in self.graph:
            for first_cord in self.graph[connection_cord]:
                g.add_edge(connection_cord, first_cord)

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
    scc = g.kosaraju()
    for component in scc:
        print(component)
    print("\n")

    print("Graf spojny:", g.is_connected())
    print("\n")

    g.display_graph()
