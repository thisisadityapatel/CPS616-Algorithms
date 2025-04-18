def compute_lps(P):
    """
    Compute the longest proper prefix which is also suffix array (LPS/failure function).
    P: pattern string of length 
    m
    Returns: list F of length m, where F[j] = length of longest prefix of P[0..j]
             that's also a suffix ending at j.
    """
    m = len(P)
    F = [0] * m
    l = 0  # length of the previous longest prefix suffix
    j = 1  # current position we are computing in F

    while j < m:
        if P[j] == P[l]:
            l += 1
            F[j] = l
            j += 1
        else:
            if l > 0:
                # fall back in the pattern
                l = F[l - 1]
            else:
                F[j] = 0
                j += 1

    return F

def kmp_search(T, P):
    """
    Find all occurrences of P in T using the KMP algorithm.
    T: text string
    P: pattern string
    Returns: list of start indices where P is found in T
    """
    n, m = len(T), len(P)
    if m == 0:
        return []  # empty pattern
    F = compute_lps(P)

    matches = []
    i = 0  # index for T
    j = 0  # index for P

    while i < n:
        if T[i] == P[j]:
            i += 1
            j += 1

            if j == m:
                matches.append(i - j)
                # continue searching from the last longest prefix
                j = F[j - 1]
        else:
            if j > 0:
                j = F[j - 1]
            else:
                i += 1
    return matches

# Example usage:
if __name__ == "__main__":
    text = "ababcabcabababd"
    pattern = "ababd"
    result = kmp_search(text, pattern)
    print(f"Pattern found at indices: {result}")
