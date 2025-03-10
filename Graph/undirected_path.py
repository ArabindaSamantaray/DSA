"""
Write a function, undirected_path, that takes in a list of edges for an undirected graph and two nodes (node_A, node_B). The function should return a boolean indicating whether or not there exists a path between node_A and node_B.
"""

def undirected_path(edges, start1, end1):
    graph = {}
    for edge in edges:
        start, end = edge
        if start not in graph.keys():
            graph[start]=[end]
        else:
            graph[start].append(end)
        if end not in graph.keys():
            graph[end]=[start]
        else:
            graph[end].append(start)
    visited = set()
    return _undirected_path(graph, start1, end1, visited)

def _undirected_path(graph, start, end, visited):
    if start==None:
        return False
    elif start==end:
        return True
    else:
        visited.add(start)
        for neighbor in graph[start]:
            if neighbor not in visited:
                if _undirected_path(graph, neighbor, end, visited):
                    return True
        return False

edges = [
  ('i', 'j'),
  ('k', 'i'),
  ('m', 'k'),
  ('k', 'l'),
  ('o', 'n')
]
print(undirected_path(edges, 'j', 'm')==True)

edges = [
  ('i', 'j'),
  ('k', 'i'),
  ('m', 'k'),
  ('k', 'l'),
  ('o', 'n')
]
print(undirected_path(edges, 'm', 'j')==True)

edges = [
  ('i', 'j'),
  ('k', 'i'),
  ('m', 'k'),
  ('k', 'l'),
  ('o', 'n')
]
print(undirected_path(edges, 'k', 'o')==False)

edges = [
  ('i', 'j'),
  ('k', 'i'),
  ('m', 'k'),
  ('k', 'l'),
  ('o', 'n')
]
print(undirected_path(edges, 'i', 'o')==False)

edges = [
  ('b', 'a'),
  ('c', 'a'),
  ('b', 'c'),
  ('q', 'r'),
  ('q', 's'),
  ('q', 'u'),
  ('q', 't'),
]
print(undirected_path(edges, 'a', 'b')==True)

edges = [
  ('b', 'a'),
  ('c', 'a'),
  ('b', 'c'),
  ('q', 'r'),
  ('q', 's'),
  ('q', 'u'),
  ('q', 't'),
]
print(undirected_path(edges, 'a', 'c')==True)

edges = [
  ('b', 'a'),
  ('c', 'a'),
  ('b', 'c'),
  ('q', 'r'),
  ('q', 's'),
  ('q', 'u'),
  ('q', 't'),
]
print(undirected_path(edges, 'r', 't')==True)

edges = [
  ('b', 'a'),
  ('c', 'a'),
  ('b', 'c'),
  ('q', 'r'),
  ('q', 's'),
  ('q', 'u'),
  ('q', 't'),
]
print(undirected_path(edges, 'r', 'b')==False)

edges = [
  ('s', 'r'),
  ('t', 'q'),
  ('q', 'r'),
]
print(undirected_path(edges, 'r', 't')==True)
