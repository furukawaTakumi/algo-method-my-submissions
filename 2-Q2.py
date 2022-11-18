import sys

sys.setrecursionlimit(10000)

n = int(input())
graph = [[] for _ in range(n)]
for current, parent in enumerate(map(int, input().split(" "))):
    graph[parent].append(current + 1)

# with open("test_file/Q2. 行きがけ順_2_input.txt", "r") as rf:
#     n = int(rf.readline())
#     graph = [[] for _ in range(n)]
#     for current, parent in enumerate(map(int, rf.readline().split(" "))):
#         graph[parent].append(current + 1)


def scanning_tree(current: int, graph: list):
    print(current)

    children = sorted(graph[current])
    for ch in children:
        scanning_tree(ch, graph)


scanning_tree(0, graph)
