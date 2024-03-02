import itertools
import sys

def calculate_distance(path, graph):
    distance = 0
    for i in range(len(path) - 1):
        distance += graph[path[i]][path[i + 1]]
    distance += graph[path[-1]][path[0]]  # Return to the starting city
    return distance

def traveling_salesman(graph):
    cities = list(graph.keys())
    min_distance = sys.maxsize
    optimal_path = None

    for path_permutation in itertools.permutations(cities):
        current_distance = calculate_distance(path_permutation, graph)
        if current_distance < min_distance:
            min_distance = current_distance
            optimal_path = path_permutation

    return optimal_path, min_distance

# Example usage:
# Create a graph representing distances between cities
graph = {
    'A': {'B': 10, 'C': 15, 'D': 20},
    'B': {'A': 10, 'C': 35, 'D': 25},
    'C': {'A': 15, 'B': 35, 'D': 30},
    'D': {'A': 20, 'B': 25, 'C': 30}
}

# Find the optimal path and minimum distance
optimal_path, min_distance = traveling_salesman(graph)

print("Optimal Path:", optimal_path)
print("Minimum Distance:", min_distance)
