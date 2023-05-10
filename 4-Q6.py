import sys

sys.setrecursionlimit(10000)

n, m = map(int, input().split())

graph = [[] for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


seen = [False for _ in range(n)]


def dfs(s: int):
    if seen[s]:
        return

    seen[s] = True

    nodes = graph[s]
    for node in nodes:
        dfs(node)


num_of_connected = 0

for index, _ in enumerate(seen):
    if seen[index]:
        continue

    dfs(index)

    num_of_connected += 1

print(num_of_connected)
