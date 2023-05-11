import sys

sys.setrecursionlimit(100000)

n, m, s, t = map(int, input().split())

graph = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())

    graph[a].append(b)


seen = [False for _ in range(n)]


def dfs(node: int):
    if seen[node]:
        return

    seen[node] = True

    neighbors = graph[node]
    for neighbor_node in neighbors:
        dfs(neighbor_node)


dfs(s)

if seen[t]:
    print("Yes")
else:
    print("No")
