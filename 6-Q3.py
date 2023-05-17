# with open("test_file/Q3. 根付き木_1_input_a.txt") as f:
#     lines = f.readlines()

# n = int(lines[0])
# m = n - 1

# graph = [[] for _ in range(n)]
# for line in lines[1::]:
#     a, b = map(int, line.split())
#     graph[a].append(b)
#     graph[b].append(a)

n = int(input())
m = n - 1


graph = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


queue = [0]
distance = [-1 for _ in range(n)]


distance[0] = 0

while len(queue) > 0:
    current_node = queue.pop(0)

    for next_node in graph[current_node]:
        if distance[next_node] != -1:
            continue

        distance[next_node] = distance[current_node] + 1
        queue.append(next_node)

print(max(distance))
