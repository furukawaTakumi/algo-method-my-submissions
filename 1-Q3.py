n, m = map(int, input().split(" "))
graph: list = [set() for _ in range(n)]

for i in range(m):
    a, b = map(int, input().split(" "))

    graph[a].add(b)
    graph[b].add(a)

num_friends = [len(friends) for friends in graph]
max_count = max(num_friends)

for friends in graph:
    if len(friends) == max_count:
        print(" ".join(map(str, sorted(friends))))
        break
