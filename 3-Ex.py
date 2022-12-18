n, m = map(int, input().split())

f_to_s = [[] for _ in range(n)]
s_to_f = [[] for _ in range(n)]

for _ in range(m):
    f, s = map(int, input().split())

    f_to_s[f].append(s)
    s_to_f[s].append(f)

queue = []
dependents = {}
seen = set()

for i in range(n):
    if len(s_to_f[i]) == 0:
        queue.append(i)
    dependents[i] = len(s_to_f[i])

while len(queue) > 0:
    current = queue.pop(0)
    seen.add(current)

    for dep_index in f_to_s[current]:
        dependents[dep_index] -= 1

        if dependents[dep_index] == 0:
            queue.append(dep_index)


if sum(dependents.values()) == 0:
    print("Yes")
else:
    print("No")
