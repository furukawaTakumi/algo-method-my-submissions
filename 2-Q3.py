import sys

sys.setrecursionlimit(10000)


n = int(input())
graph = [[] for _ in range(n)]

for i, pi in enumerate(map(int, input().split(" "))):
    graph[pi].append(i + 1)

answer = {}


def scanning_tree(current: int, graph: list, depth: int):
    answer[current] = depth
    children = sorted(graph[current])
    for child in children:
        scanning_tree(child, graph, depth + 1)


scanning_tree(0, graph, 0)

for i, v in sorted(answer.items(), key=lambda x: x[0]):
    print(v)
