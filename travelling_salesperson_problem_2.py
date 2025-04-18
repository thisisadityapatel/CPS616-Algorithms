w = [[0, 29, 20, 21], [29, 0, 15, 17], [20, 15, 0, 28], [21, 17, 28, 0]]

OptW = float("inf")
OptX = None
n = 4
X = [-1] * n
l = 0


def calculate_total_weight(path, l=None):
    global n, w
    weight = 0
    if not l:
        l = n
    for i in range(l - 1):
        weight += w[path[i]][path[i + 1]]
    weight += w[path[-1]][path[0]]
    return weight


def calculate_bound_value(X, l):
    cost = sum(w[X[i]][X[i + 1]] for i in range(l - 1))
    saved = w[X[l - 1]][X[0]]
    if l < n:
        w[X[l - 1]][X[0]] = float("inf")

    Y = set(range(n)) - set(X[:l])
    XT = Y | {X[l - 1]}  # tails
    XH = Y | {X[0]}  # heads

    r = {}
    for i in XT:
        r[i] = min(w[i][j] for j in XH)
        cost += r[i]

    for j in XH:
        cost += min(w[i][j] - r[i] for i in XT)

    if l < n:
        w[X[l - 1]][X[0]] = saved

    return cost


def bounded_backtrack(X, l):
    global OptX, OptW, n, w
    if l == n:
        total_weight = calculate_total_weight(X)
        if total_weight < OptW:
            OptW = total_weight
            OptX = X[:]
    else:
        Options = {0}
        if l > 0:
            Options = set(range(1, n))
            bound_cost = calculate_bound_value(X, l)
            if bound_cost >= OptW:
                return
        Options = Options - set(X[:l])
        for option in Options:
            X[l] = option
            bounded_backtrack(X, l + 1)


bounded_backtrack(X, l)
print(OptX)
print(OptW)
