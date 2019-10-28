graph={
    1:[2,3],
    2:[1,4,5,7],
    3:[1,5,9],
    4:[2,6],
    5:[2,3,7,8],
    6:[4],
    7:[5,2],
    8:[5],
    9:[3],
}

def BFS(graph, root):
  visited = []
  queue = [root]
  while queue:
    n = queue.pop(0)
    if n not in visited:
      visited.append(n)
    for i in graph[n]:
      if i not in visited:
        queue.append(i)
  return visited

print(BFS(graph, 1))