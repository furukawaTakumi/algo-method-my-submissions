import sys

n = int(input())
graph = [[] for _ in range(n)]
costs = {i: dict() for i in range(n)}
for index, a in enumerate(map(int, input().split())):
    costs[index][index + 1] = a
    graph[index].append(index + 1)

for index, b in enumerate(map(int, input().split())):
    costs[index][index + 2] = b
    graph[index].append(index + 2)


distance = [sys.maxsize for _ in range(n)]
distance[0] = 0
distance[1] = distance[0] + costs[0][1]

for i in range(2, n):
    distance[i] = min(
        distance[i - 1] + costs[i - 1][i], distance[i - 2] + costs[i - 2][i]
    )

print(distance[-1])
