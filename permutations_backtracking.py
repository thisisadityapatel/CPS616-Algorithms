# permutations of a list of numbers
n = 4
X = [0] * n
l = 0

def permutations(X, l, n):
    # if the list X has reached the full length
    if l == n:
        print(X)
    else:
        # all the available number options that are not yet included in the X list
        Options = set(range(n)) - set(X[:l])
        # going through each of the option combination
        for option in Options:
            X[l] = option
            permutations(X, l + 1, n)

permutations(X, l, n)