"""
Write a function, has_cycle, that takes in an object representing the adjacency list of a directed graph. The function should return a boolean indicating whether or not the graph contains a cycle.

Ideal algorithm is white-grey-black

But basically perform a DFS with each node as a starting point, in that DFS traversal if any node gets repeated then it will be a cycle
"""

def has_cycle(graph):
    for node in graph.keys():
        visited = set()
        if dfs_traversal(graph, node, visited):
            return True
    return False

def dfs_traversal(graph, start, visited):
    if start==None:
        return False
    elif start in visited:
        return True
    else:
        visited.add(start)
        for neighbor in graph[start]:
            return dfs_traversal(graph, neighbor, visited)



print(has_cycle({
  "a": ["b"],
  "b": ["c"],
  "c": ["a"],
})==True)

print(has_cycle({
  "a": ["b", "c"],
  "b": ["c"],
  "c": ["d"],
  "d": [],
})==False)


print(has_cycle({
  "a": ["b", "c"],
  "b": [],
  "c": [],
  "e": ["f"],
  "f": ["e"],
})==True)


print(has_cycle({
  "q": ["r", "s"],
  "r": ["t", "u"],
  "s": [],
  "t": [],
  "u": [],
  "v": ["w"],
  "w": [],
  "x": ["w"],
})==False)


print(has_cycle({
  "a": ["b"],
  "b": ["c"],
  "c": ["a"],
  "g": [],
})==True)


print(has_cycle({
  "a": ["b"],
  "b": ["c"],
  "c": ["d"],
  "d": ["b"],
})==True)


print(has_cycle({
  "a": ["b", "c"],
  "b": ["c"],
  "c": ["d"],
  "d": [],
  "e": ["c"],
})==False)

