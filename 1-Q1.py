
n, a, b = map(int, input().split(' '))
graph = [[] for _ in range(n)]

for i in range(n):
    friend_string = input()

    for j, j_ox in enumerate(friend_string):
        if j_ox == 'o':
            graph[i].append(j)
            graph[j].append(i)

if a in graph[b]:
    print('Yes')
else: 
    print('No')


