import sys

sys.setrecursionlimit(100000)

n, m = map(int, input().split())

graph = {i: [] for i in range(n)}
seen = set()

for _ in range(m):
    a, b = map(int, input().split())

    graph[a].append(b)


preorder = []


def dfs(current_vertex: int):
    seen.add(current_vertex)

    preorder.append(current_vertex)

    for next_vertex in sorted(graph[current_vertex]):
        if next_vertex in seen:
            continue

        dfs(next_vertex)


dfs(0)

print(" ".join(map(str, preorder)))
