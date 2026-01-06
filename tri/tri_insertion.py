def tri_insertion(tab):
    n = len(tab)
    for p in range(1, n):
        key = tab[p]
        i = p - 1
        while i >= 0 and tab[i] > key:
            tab[i + 1] = tab[i]
            i -= 1
        tab[i + 1] = key
    return tab