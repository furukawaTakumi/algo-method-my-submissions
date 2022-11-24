import sys

sys.setrecursionlimit(10000)

n = int(input())

graph = [[] for _ in range(n)]

for i, pi in enumerate(map(int, input().split(" ")), 1):
    graph[pi].append(i)

answers = {}


def dfs(current: int, graph: list):
    descendants = 1
    for child in graph[current]:
        descendants += dfs(child, graph)

    answers[current] = descendants - 1
    return descendants


dfs(0, graph)

[print(answer[1]) for answer in sorted(answers.items(), key=lambda x: x[0])]
