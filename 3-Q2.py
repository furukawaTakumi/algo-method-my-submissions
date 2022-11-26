n, m = map(int, input().split())

graph = [[] for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())

    graph[a].append(b)
    graph[b].append(a)


destination_costs = {0: 0}

queue = [0]
seen = set([0])

while len(queue) > 0:
    current = queue.pop(0)

    for next_vertex in graph[current]:
        if next_vertex in seen:
            continue

        seen.add(next_vertex)
        queue.append(next_vertex)
        destination_costs[next_vertex] = destination_costs[current] + 1


print(max(destination_costs.values()))
