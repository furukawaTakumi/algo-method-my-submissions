from collections import defaultdict

h, w = map(int, input().split())
x0, y0, x1, y1 = map(int, input().split())
start, goal = (x0, y0), (x1, y1)

graph = defaultdict(lambda: [])
seen = set()

before_s = ""
for i in range(h):
    s = input()
    for j in range(w):
        if j + 1 < len(s):
            if "W" == s[j] == s[j + 1]:
                graph[(i, j)].append((i, j + 1))
                graph[(i, j + 1)].append((i, j))

        if i > 0:
            if "W" == before_s[j] == s[j]:
                graph[(i, j)].append((i - 1, j))
                graph[(i - 1, j)].append((i, j))

    before_s = s

destination_costs = defaultdict(lambda: 0)
queue = [start]


while len(queue) > 0:
    current = queue.pop(0)
    seen.add(current)

    for next_vertex in graph[current]:
        if next_vertex in seen:
            continue

        queue.append(next_vertex)
        destination_costs[next_vertex] = destination_costs[current] + 1


print(destination_costs[goal])
