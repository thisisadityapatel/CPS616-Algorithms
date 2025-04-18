profits = [92, 57, 49, 68, 60, 43, 67, 84, 87, 72]
weights = [23, 31, 29, 44, 53, 38, 63, 85, 89, 82]
capacity = 165

OptX = None
OptW = 0
OptP = float("-inf")

n = 10
X = [0] * n
l = 0


def knapsack(X, l, n):
    global profits, weights, capacity, OptX, OptW, OptP

    current_profit = sum([profits[i] * X[i] for i in range(l)])
    current_weight = sum([weights[i] * X[i] for i in range(l)])

    if l == n:
        if current_profit > OptP:
            OptP = current_profit
            OptW = current_weight
            OptX = X.copy()
    else:
        Options = {0}
        if current_weight + weights[l] <= capacity:
            Options = {0, 1}
        for option in Options:
            X[l] = option
            knapsack(X, l + 1, n)


knapsack(X, l, n)
print(OptP)
print(OptW)
print(OptX)
