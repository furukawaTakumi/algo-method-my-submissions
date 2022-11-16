n, x = map(int, input().split(" "))
a = tuple(map(int, input().split(" ")))

# トレース用
# print(" ".join([str(index).zfill(2) for index in range(len(a))]))
# print(" ".join([str(n).zfill(2) for n in a]))


def solve(a, target: int, sum) -> int:
    if a[target] == 0:
        return sum
    return solve(a, a[target] - 1, sum + 1)


print(solve(a, x - 1, 1))
