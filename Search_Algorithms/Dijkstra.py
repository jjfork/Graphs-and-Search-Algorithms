import random
import heapq
import networkx as nx
import matplotlib.pyplot as plt


class Graph:
    def __init__(self):
        self.nodes = {}

    def add_node(self, node):
        self.nodes[node] = {}

    def add_edge(self, main_node, sub_node, weight):
        self.nodes[main_node][sub_node] = weight
        self.nodes[sub_node][main_node] = weight

    def set_paths(self, main_node, **kwargs):
        for sub_node, weight in kwargs.items():
            self.add_edge(main_node, sub_node, weight)

    def dijkstra(self, first_node):
        distances = {node: float('inf') for node in self.nodes}
        distances[first_node] = 0
        visited = set()
        end = {}

        queue = [(0, first_node)]

        while queue:
            current_distance, curr_node = heapq.heappop(queue)

            if curr_node in visited:
                continue

            visited.add(curr_node)

            for next, weight in self.nodes[curr_node].items():
                distance = current_distance + weight

                if distance < distances[next]:
                    distances[next] = distance
                    end[next] = curr_node
                    heapq.heappush(queue, (distance, next))

        return distances, end


def calculate_paths():
    global all_paths, node, target_node, path
    all_paths = {}
    for node in graph.nodes:
        distances, previous = graph.dijkstra(node)
        path_info = {}
        for target_node in distances:
            if target_node != node:
                path = []
                current_node = target_node
                while current_node != node:
                    path.append(current_node)
                    current_node = previous[current_node]
                path.append(node)
                path.reverse()
                path_weight = sum(graph.nodes[path[i]][path[i + 1]] for i in range(len(path) - 1))
                path_info[target_node] = path_weight
        all_paths[node] = path_info


def create_graph():
    global graph
    # Create the graph
    graph = Graph()
    # Add nodes
    graph.add_node('A')
    graph.add_node('B')
    graph.add_node('C')
    graph.add_node('D')
    graph.add_node('E')
    graph.add_node('F')
    graph.add_node('G')
    # Set paths from node A
    graph.set_paths('A', B=5, G=5)
    # Set paths from node B
    graph.set_paths('B', C=3, D=3, G=5)
    # Set paths from node C
    graph.set_paths('C', D=1, B=3)
    # Set paths from node D
    graph.set_paths('D', C=1, B=3, G=3, E=5)
    # Set paths from node E
    graph.set_paths('E', F=2, D=5)
    # Set paths from node F
    graph.set_paths('F', G=5, D=4, E=2)
    graph.set_paths('G', A=5, B=5, D=3, F=5)


create_graph()


def display_paths():
    global node, paths, target_node, weight, path
    print("Paths:")
    printed_paths = set()
    for node, paths in all_paths.items():
        for target_node, weight in paths.items():
            path = f"{node} - {target_node}"
            if path not in printed_paths:
                print(f"{path} : {weight}")
                printed_paths.add(path)


def vizualize_graph():
    global nx_graph, pos
    # Visualize the graph
    nx_graph = nx.Graph(graph.nodes)
    pos = nx.spring_layout(nx_graph)
    nx.draw(nx_graph, pos, with_labels=True)


def add_path_labels():
    global path_labels, node, paths, target_node, weight, path
    # Add path labels (connection weights) to the graph visualization
    path_labels = {}
    for node, paths in all_paths.items():
        for target_node, weight in paths.items():
            path = f"{node} - {target_node}"
            path_labels[(node, target_node)] = f"{path}: {weight}"


def vizualize_edges():
    edge_labels = nx.get_edge_attributes(nx_graph, 'weight')
    nx.draw_networkx_edge_labels(nx_graph, pos, edge_labels=edge_labels, font_color='red', label_pos=0.5)


calculate_paths()


display_paths()


vizualize_graph()


vizualize_edges()


add_path_labels()

nx.draw_networkx_edge_labels(nx_graph, pos, edge_labels=path_labels, font_color='blue', label_pos=0.5, rotate=False)

plt.show()
