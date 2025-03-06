"""
Write a BFS traversal for a graph
"""

graph={
        "a":["b", "c"],
        "b":["d"],
        "c":["e"],
        "d":["f"],
        "e":[],
        "f":[]
        }

def bfs_traversal(graph, start):
    queue = [start]
    result = []
    while len(queue)!=0:
        node = queue.pop(0)
        result.append(node)
        for neighbors in graph[node]:
            queue.append(neighbors)
    return result

print(bfs_traversal(graph, "a")==["a", "b", "c", "d", "e", "f"])
