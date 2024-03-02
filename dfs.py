class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    def dfs(self, start, visited):
        visited[start] = True
        print(start, end=' ')

        if start in self.graph:
            for neighbor in self.graph[start]:
                if not visited[neighbor]:
                    self.dfs(neighbor, visited)

    def dfs_traversal(self, start):
        visited = {node: False for node in self.graph}
        self.dfs(start, visited)

# Example usage:
# Create a graph and add edges
my_graph = Graph()
my_graph.add_edge(0, 1)
my_graph.add_edge(0, 2)
my_graph.add_edge(1, 2)
my_graph.add_edge(2, 0)
my_graph.add_edge(2, 3)
my_graph.add_edge(3, 3)

# Perform DFS traversal starting from vertex 2
print("DFS Traversal starting from vertex 2:")
my_graph.dfs_traversal(2)
