def add_edge(graph, u, v):
    graph[u].append(v)

def dfs(graph, start):
    visited = set([start])
    stack = [start]

    while stack:
        node = stack.pop()
        print(node, end=" ")

        for i in graph[node]:
            if i not in visited:
                stack.append(i)
                visited.add(i)

graph = {i: [] for i in range(4)}
add_edge(graph, 0, 1)
add_edge(graph, 0, 2)
add_edge(graph, 1, 2)
add_edge(graph, 2, 0)
add_edge(graph, 2, 3)
add_edge(graph, 3, 3)

print("Following is Depth First Traversal (starting from vertex 2)")
dfs(graph, 2)