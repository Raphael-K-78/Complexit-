def tri_a_bulle(tab):
    n = len(tab)
    permut = True
    while permut:
        permut = False
        for i in range(n-1):
            if tab[i] > tab[i+1]:
                tab[i], tab[i+1] = tab[i+1], tab[i]
                permut = True
    return tab