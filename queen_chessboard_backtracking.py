# N‑Queens backtracking
# We encode the board with a single list X.
# The board is n × n, and each row contains exactly one queen.
# The list index i represents row i.
# The value X[i] is the column where the queen in row i is placed.


def backtracking(X, l, n):
    if l == n:
        print(X)
    else:
        # All the columns options that are not already previously present in X.
        Options = set(range(1, n + 1)) - set(X[:l])

        # Going through each of the previously selected queen till index l, and removing the column option where the queen would conflict with the diagonal or the back diagonal position.
        for i in range(l):
            row = i
            col = X[i]
            Options.discard(col - (l - row))
            Options.discard(col + (l - row))

        for option in Options:
            X[l] = option
            backtracking(X, l + 1, n)


n = 4
X = [0] * n
l = 0

backtracking(X, l, n)
