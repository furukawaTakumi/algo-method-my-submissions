n, m = map(int, input().split(" "))
graph: list = [[] for _ in range(n)]

# フォロー関係の入力
for _ in range(m):
    a, b = map(int, input().split(" "))

    graph[a].append(b)

# 出力の表示
for i in range(n):
    if len(graph[i]):
        print(" ".join(map(str, sorted(graph[i]))))
    else:
        print()
