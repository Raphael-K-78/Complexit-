def tri_casier(tab):
    a, b = min(tab), max(tab)
    T = [0] * (b - a + 1)
    for x in tab:
        T[x - a] += 1
    result = []
    for i, count in enumerate(T):
        result.extend([i + a] * count)
    return result