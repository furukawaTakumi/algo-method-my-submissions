import sys

sys.setrecursionlimit(100000)


n, m = map(int, input().split())

graph = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

for idx in range(n):
    graph[idx].sort()

seen = [False for _ in range(n)]

order = []


def rec(v: int):
    seen[v] = True
    for v2 in graph[v]:
        if seen[v2]:
            continue
        rec(v2)

    order.append(v)


for v in range(n):
    if seen[v]:
        continue
    rec(v)

order.reverse()
print(" ".join(map(str, order)))
