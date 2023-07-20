n, m, s, t = map(int, input().split())

graph = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)


def create_origins(s: int, graph: list):
    seen = [False for _ in range(len(graph))]
    origin = [-1 for _ in range(len(graph))]
    queue = [s]

    while len(queue) > 0:
        current = queue.pop()

        for next_node in graph[current]:
            if seen[next_node]:
                continue

            seen[next_node] = True
            queue.append(next_node)
            origin[next_node] = current
    return origin


def is_st_path(path: list):
    if len(path) == 0:
        return False
    return path[0] == s and path[-1] == t


def backprops(origin: list):
    st_path = []
    current = t
    while not is_st_path(st_path[::-1]):
        st_path.append(current)
        current = origin[current]
    return st_path[::-1]


origins = create_origins(s, graph)
st_path = backprops(origins)
print(len(st_path))
print(" ".join(map(str, st_path)))
