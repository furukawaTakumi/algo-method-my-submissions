n, m = map(int, input().split())

graph = {vertex_number: [] for vertex_number in range(n)}
seen = set()

for _ in range(m):
    a, b = map(int, input().split())

    graph[a].append(b)


def dfs(current_vertex: int):
    seen.add(current_vertex)

    for next_vertex in graph[current_vertex]:
        if next_vertex in seen:
            continue

        dfs(next_vertex)


dfs(0)

print(n - len(seen))
