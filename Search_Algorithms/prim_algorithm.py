import random


class PrimAlgorithm:
    def __init__(self, graph):
        self.graph = graph

    def find_min_edge(self, visited):
        min_edge = None

        for edge in self.graph.edges:
            u, v, weight = edge
            if (u in visited and v not in visited) or (u not in visited and v in visited):
                if min_edge is None or weight < min_edge[2]:
                    min_edge = edge

        return min_edge

    def find_mst(self):
        mst = []
        start_vertex = random.choice(self.graph.vertices)
        visited = {start_vertex}

        while len(visited) < len(self.graph.vertices):
            min_edge = self.find_min_edge(visited)

            if min_edge is not None:
                mst.append(min_edge)
                u, v, _ = min_edge
                visited.add(u)
                visited.add(v)

        return mst
