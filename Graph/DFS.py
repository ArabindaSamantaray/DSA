"""
Get the DFS traversal for a graph
"""

graph={
        "a":["b", "c"],
        "b":["d"],
        "c":["e"],
        "d":["f"],
        "e":[],
        "f":[]
        }

def dfs_traversal(graph, start, visited):
    if start==None:
        return []
    else:
        visited.append(start)
        for neighbor in graph[start]:
            dfs_traversal(graph, neighbor, visited)

visited = []
dfs_traversal(graph, "a", visited)
print(visited)
