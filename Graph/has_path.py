"""
Write a function, has_path, that takes in a dictionary representing the adjacency list of a directed acyclic graph and two nodes (src, dst). The function should return a boolean indicating whether or not there exists a directed path between the source and destination nodes.
"""

def has_path(graph, start, end):
    if start==None:
        return False
    elif start==end:
        return True
    else:
        for neighbor in graph[start]:
            if has_path(graph, neighbor, end):
                return True
        return False



graph = {
  'f': ['g', 'i'],
  'g': ['h'],
  'h': [],
  'i': ['g', 'k'],
  'j': ['i'],
  'k': []
}
print(has_path(graph, 'f', 'k')==True)

graph = {
  'f': ['g', 'i'],
  'g': ['h'],
  'h': [],
  'i': ['g', 'k'],
  'j': ['i'],
  'k': []
}
print(has_path(graph, 'f', 'j')==False)

graph = {
  'f': ['g', 'i'],
  'g': ['h'],
  'h': [],
  'i': ['g', 'k'],
  'j': ['i'],
  'k': []
}
print(has_path(graph, 'i', 'h')==True)

graph = {
  'v': ['x', 'w'],
  'w': [],
  'x': [],
  'y': ['z'],
  'z': [],
}
print(has_path(graph, 'v', 'w')==True)

graph = {
  'v': ['x', 'w'],
  'w': [],
  'x': [],
  'y': ['z'],
  'z': [],
}
print(has_path(graph, 'v', 'z')==False)
