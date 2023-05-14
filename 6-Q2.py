h, w = map(int, input().split())

grid_vertex = h * w
tree_edges = grid_vertex - 1

grid_edges = (h - 1) * w + (w - 1) * h

removal_edges = grid_edges - tree_edges

print(removal_edges)
