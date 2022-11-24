import sys

sys.setrecursionlimit(10000)

n = int(input())

graph = [[] for _ in range(n + 1)]

for i, pi in enumerate(map(int, input().split(" ")), 1):
    graph[pi].append(i)

max_depth = -1


def dfs(current: int, graph: list, depth=0) -> None:
    global max_depth

    if max_depth < depth:
        max_depth = depth

    for child in graph[current]:
        dfs(child, graph, depth + 1)


dfs(0, graph, 0)
print(max_depth)
