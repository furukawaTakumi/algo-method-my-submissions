n = int(input())
m = n - 1


graph = [[] for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())

    graph[a].append(b)
    graph[b].append(a)


def prepare_lists(graph: list):
    parent_list = [-1 for _ in range(len(graph))]
    children_list = [[] for _ in range(len(graph))]
    seen = [False for _ in range(len(graph))]
    queue = [0]

    while len(queue) > 0:
        current_node = queue.pop(0)

        seen[current_node] = True

        for child_node in graph[current_node]:
            if seen[child_node]:
                continue

            queue.append(child_node)

            parent_list[child_node] = current_node
            children_list[current_node].append(child_node)

    degree_list = [0 for _ in range(len(graph))]
    leafs = []
    for i in range(len(graph)):
        degree_list[i] = len(children_list[i])

        if len(children_list[i]) == 0:
            leafs.append(i)

    return parent_list, children_list, degree_list, leafs


parent_list, children_list, degree_list, leafs = prepare_lists(graph)
is_selected = [False for _ in range(n)]


while len(leafs) > 0:
    current_node = leafs.pop()

    is_child_selected = False

    for child in children_list[current_node]:
        is_child_selected |= is_selected[child]

    is_selected[current_node] = not is_child_selected

    parent = parent_list[current_node]
    degree_list[parent] -= 1

    if degree_list[parent] == 0:
        leafs.append(parent)

print(sum(is_selected))
