import sys

sys.setrecursionlimit(10000)

n, m = map(int, input().split())

graph = [[] for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())

    graph[a].append(b)
    graph[b].append(a)

seen: set = set()


def dfs(current: int):
    seen.add(current)
    for next in graph[current]:
        if next in seen:
            continue

        dfs(next)


dfs(0)


if len(seen) == len(graph):
    print("Yes")
else:
    print("No")
