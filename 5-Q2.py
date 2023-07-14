import sys

sys.setrecursionlimit(1000000)

# with open("test_file/Q2. s-t パス (D)_1_input.txt", "r") as f:
#     lines = f.readlines()
# n, m, s, t = map(int, lines[0].split())
# graph = [[] for _ in range(n)]
# for line in lines[1:]:
#     a, b = map(int, line.split())
#     graph[a].append(b)

n, m, s, t = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

st_path = []


def create_search_path(s: int, t: int):
    def is_st_path(st_path: list):
        if not len(st_path):
            return False
        return st_path[0] == s and st_path[-1] == t

    seen = [False for _ in range(n)]

    def search_path_by_dfs(current_node: int, graph: list, st_path=(s,)) -> tuple:
        if is_st_path(st_path):
            return st_path

        if seen[current_node]:
            return st_path[:-1]

        seen[current_node] = True

        for child_node in graph[current_node]:
            st_path = search_path_by_dfs(child_node, graph, st_path + (child_node,))

            if is_st_path(st_path):
                return st_path

        return st_path[:-1]

    return search_path_by_dfs


search_st_path = create_search_path(s, t)
result = search_st_path(s, graph)
print(len(result))
print(" ".join(map(str, result)))
