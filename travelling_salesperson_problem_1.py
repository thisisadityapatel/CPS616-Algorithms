w = [[0, 29, 20, 21], [29, 0, 15, 17], [20, 15, 0, 28], [21, 17, 28, 0]]

OptX = None
OptW = float("inf")
n = 4
X = [-1] * n


def calculate_total_weight(path, l):
    weight = 0
    for i in range(l - 1):
        weight += w[path[i]][path[i + 1]]
    weight += w[path[-1]][path[0]]
    return weight


def backtrack(X, l):
    global OptW, OptX
    if l == n:
        total_weight = calculate_total_weight(X, l)
        if total_weight < OptW:
            OptW = total_weight
            OptX = X[:]
    else:
        if l == 0:
            Options = {0}
        else:
            Options = set(range(1, n))
        Options = Options - set(X[:l])
        for option in Options:
            X[l] = option
            backtrack(X, l + 1)


backtrack(X, 0)
print("optimal path:", OptX + [OptX[0]])
print("minimul cost:", OptW)
