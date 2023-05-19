n = int(input())
m = n - 1

graph = [[] for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def bfs(start: int, graph: list):
    queue = [start]

    distance = [-1 for _ in range(n)]
    distance[start] = 0

    while len(queue) > 0:
        current_node = queue.pop(0)

        for next_node in graph[current_node]:
            if distance[next_node] != -1:
                continue

            distance[next_node] = distance[current_node] + 1
            queue.append(next_node)

    return distance


maximum = 0
for node in range(n):
    distance = bfs(node, graph)
    maximum = max(maximum, max(distance))


print(maximum)
