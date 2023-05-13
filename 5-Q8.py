import sys

sys.setrecursionlimit(100000)

n, m = map(int, input().split())

graph = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)


seen = [False for _ in range(n)]
finished = [False for _ in range(n)]
has_cycle: bool = False


def dfs(node: int):
    global has_cycle

    if seen[node]:
        if not finished[node]:
            has_cycle = True
        return

    seen[node] = True

    for next_node in graph[node]:
        dfs(next_node)

    finished[node] = True


for i in range(n):
    if seen[i]:
        continue
    dfs(i)

if has_cycle:
    print("Yes")
else:
    print("No")
