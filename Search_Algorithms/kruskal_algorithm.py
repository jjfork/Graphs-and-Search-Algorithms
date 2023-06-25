class KruskalAlgorithm:
    def __init__(self, graph):
        self.graph = graph

    def find_mst(self):
        mst = []
        sorted_edges = sorted(self.graph.edges, key=lambda x: x[2])

        parent = {vertex: vertex for vertex in self.graph.vertices}
        rank = {vertex: 0 for vertex in self.graph.vertices}

        def find(vertex):
            if parent[vertex] != vertex:
                parent[vertex] = find(parent[vertex])
            return parent[vertex]

        def union(vertex1, vertex2):
            root1 = find(vertex1)
            root2 = find(vertex2)
            if rank[root1] < rank[root2]:
                parent[root1] = root2
            elif rank[root1] > rank[root2]:
                parent[root2] = root1
            else:
                parent[root2] = root1
                rank[root1] += 1

        for edge in sorted_edges:
            u, v, weight = edge
            if find(u) != find(v):
                mst.append(edge)
                union(u, v)

        return mst
