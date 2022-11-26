from collections import defaultdict

n, m = map(int, input().split())

graph = [[] for _ in range(n)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

destination_costs = [-1] * n

queue = [0]

destination_costs[0] = 0

k = 0

seen = set([0])

cost_to_nodes = defaultdict(lambda: [])

while len(queue) > 0:
    current = queue.pop(0)

    cost_to_nodes[destination_costs[current]].append(current)

    for next_vertex in graph[current]:
        if next_vertex in seen:
            continue

        destination_costs[next_vertex] = destination_costs[current] + 1
        queue.append(next_vertex)
        seen.add(next_vertex)


for nodes in cost_to_nodes.values():
    print(" ".join([str(node) for node in sorted(nodes)]))
