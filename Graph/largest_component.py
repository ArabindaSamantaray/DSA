"""
Write a function, largest_component, that takes in the adjacency list of an undirected graph. The function should return the size of the largest connected component in the graph.
"""


def largest_component(graph):
    visited = set()
    max_component_size = 0
    for node in graph.keys():
        if node not in visited:
            size = bfs_traversal(graph, node, visited)
            if size > max_component_size:
                max_component_size = size
    return max_component_size

def bfs_traversal(graph, start, visited):
    queue=[start]
    visited.add(start)
    size = 0
    while len(queue)!=0:
        node = queue.pop(0)
        size = size+1
        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)
    return size




print(largest_component({
  0: [8, 1, 5],
  1: [0],
  5: [0, 8],
  8: [0, 5],
  2: [3, 4],
  3: [2, 4],
  4: [3, 2]
})==4)

print(largest_component({
  1: [2],
  2: [1,8],
  6: [7],
  9: [8],
  7: [6, 8],
  8: [9, 7, 2]
})==6)

print(largest_component({
  3: [],
  4: [6],
  6: [4, 5, 7, 8],
  8: [6],
  7: [6],
  5: [6],
  1: [2],
  2: [1]
})==5)

print(largest_component({})==0)

print(largest_component({
  0: [4,7],
  1: [],
  2: [],
  3: [6],
  4: [0],
  6: [3],
  7: [0],
  8: []
}) == 3)
