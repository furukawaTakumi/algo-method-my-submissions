from queue import Queue
import itertools

n, m = map(int, input().split(" "))

graph = [[] for _ in range(n)]

for i in range(m):
    a, b = map(int, input().split(" "))
    graph[a].append(b)
    graph[b].append(a)

destination_costs = [-1 for _ in range(n)]

queue = Queue()
queue.put(0)

destination_costs[0] = 0

k = 0

seen = set([0])

while not queue.empty():
    current = queue.get()

    for next_vertex in graph[current]:
        if next_vertex in seen:
            continue

        destination_costs[next_vertex] = destination_costs[current] + 1
        queue.put(next_vertex)
        seen.add(next_vertex)


for group_num, nums in itertools.groupby(
    sorted(enumerate(destination_costs), key=lambda x: x[1]), key=lambda x: x[1]
):
    if group_num == -1:
        continue
    print(" ".join([str(num[0]) for num in nums]))
