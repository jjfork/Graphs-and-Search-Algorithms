import heapq
import networkx as nx

class Graph:
    def __init__(self):
        self.nodes = {}

    def add_node(self, node):
        self.nodes[node] = {}

    def add_edge(self, node1, node2, weight):
        self.nodes[node1][node2] = weight
        self.nodes[node2][node1] = weight

    def dijkstra(self, start_node):
        distances = {node: float('inf') for node in self.nodes}
        distances[start_node] = 0
        visited = set()
        previous = {}

        priority_queue = [(0, start_node)]

        while priority_queue:
            current_distance, current_node = heapq.heappop(priority_queue)

            if current_node in visited:
                continue

            visited.add(current_node)

            for neighbor, weight in self.nodes[current_node].items():
                distance = current_distance + weight

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous[neighbor] = current_node
                    heapq.heappush(priority_queue, (distance, neighbor))

        return distances, previous

# Create the graph
graph = Graph()

# Add nodes
graph.add_node('a')
graph.add_node('b')
graph.add_node('c')
graph.add_node('d')
graph.add_node('e')

# Add edges
graph.add_edge('a', 'b', 5)
graph.add_edge('a', 'c', 8)
graph.add_edge('b', 'd', 9)
graph.add_edge('c', 'd', 2)
graph.add_edge('c', 'e', 7)
graph.add_edge('d', 'e', 6)

# Calculate paths using Dijkstra's algorithm
distances, previous = graph.dijkstra('a')

# Display the results
print("Start node:", 'a')
print("Visited vertices:", list(distances.keys()))
print("Sum of paths:", sum(distances.values()))
print("")

# Present the paths in a table format
print("Paths:")
for node in distances:
    if node == 'a':
        continue

    path = []
    current = node

    while current != 'a':
        path.append(current)
        current = previous[current]

    path.append('a')
    path.reverse()
    print(f"{node} - {' - '.join(path)} : {distances[node]}")

# Check if these are the shortest paths
shortest_paths = {
    'a': {'b': 5, 'c': 8},
    'b': {'a': 5, 'd': 9},
    'c': {'a': 8, 'd': 2, 'e': 7},
    'd': {'b': 9, 'c': 2, 'e': 6},
    'e': {'c': 7, 'd': 6}
}

are_shortest_paths = all(shortest_paths[node].get(neighbor, float('inf')) == distances[neighbor]
                         for node in shortest_paths
                         for neighbor in shortest_paths[node])

print("")
print("Are these the shortest paths?", are_shortest_paths)

# Create a NetworkX graph
nx_graph = nx.Graph()

# Add nodes and edges to the NetworkX graph
for node in graph.nodes:
    nx_graph.add_node(node)

for node1, neighbors in graph.nodes.items():
    for node2, weight in neighbors.items():
        nx_graph.add_edge(node1, node2, weight=weight)

# Visualize the graph
pos = nx.spring_layout(nx_graph)
