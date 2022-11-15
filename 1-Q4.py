n, m, x = map(int, input().split(" "))
graph = [set() for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split(" "))

    graph[a].add(b)
    graph[b].add(a)


friends_of_friends = set()
for aruru_friend in graph[x]:
    friends_of_friends = friends_of_friends | set(graph[aruru_friend]) - set(
        graph[x]
    ) - set([x])

print(len(friends_of_friends))
