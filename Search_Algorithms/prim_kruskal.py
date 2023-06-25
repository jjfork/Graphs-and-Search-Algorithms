import string
import random
import time
import matplotlib.pyplot as plt
from prim_algorithm import PrimAlgorithm
from kruskal_algorithm import KruskalAlgorithm


class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.edges = []

    def add_edge(self, u, v, weight):
        self.edges.append((u, v, weight))


def create_random_graph(n):
    vertices = string.ascii_uppercase[:n]
    graph = Graph(vertices)

    for vertex in vertices:
        num_paths = random.randint(1, n)
        for _ in range(num_paths):
            weight = random.randint(1, n)
            random_vertex = random.choice(vertices)
            graph.add_edge(vertex, random_vertex, weight)

    return graph


def monte_carlo_comparison(n_values, iterations):
    prim_times = []
    kruskal_times = []

    for n in n_values:
        prim_avg_time = 0
        kruskal_avg_time = 0

        for _ in range(iterations):
            graph = create_random_graph(n)

            prim_avg_time = calc_prime_time(graph, prim_avg_time)

            kruskal_avg_time = calc_kruskal_time(graph, kruskal_avg_time)

        prim_avg_time /= iterations
        kruskal_avg_time /= iterations

        prim_times.append(prim_avg_time)
        kruskal_times.append(kruskal_avg_time)

    return prim_times, kruskal_times


def calc_prime_time(graph, prim_avg_time):
    prim_algorithm = PrimAlgorithm(graph)
    start_time = time.perf_counter_ns()
    prim_algorithm.find_mst()
    prim_time = time.perf_counter_ns() - start_time
    prim_avg_time += prim_time
    return prim_avg_time


def calc_kruskal_time(graph, kruskal_avg_time):
    kruskal_algorithm = KruskalAlgorithm(graph)
    start_time = time.perf_counter_ns()
    kruskal_algorithm.find_mst()
    kruskal_time = time.perf_counter_ns() - start_time
    kruskal_avg_time += kruskal_time
    return kruskal_avg_time


def plot_comparison(n_values, prim_times, kruskal_times):
    plt.plot(n_values, prim_times, label="Prim's Algorithm")
    plt.plot(n_values, kruskal_times, label="Kruskal's Algorithm")
    plt.xlabel('Number of Elements')
    plt.ylabel('Average Time (nanoseconds)')
    plt.title('Comparison of Prim\'s and Kruskal\'s Algorithms')
    plt.legend()
    plt.show()


n_values = [5, 10, 15, 20]
iterations = 100

prim_times, kruskal_times = monte_carlo_comparison(n_values, iterations)
plot_comparison(n_values, prim_times, kruskal_times)
