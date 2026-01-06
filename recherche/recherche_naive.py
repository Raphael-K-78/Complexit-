def recherche_naive(tab, cible):
    for i in range(len(tab)):
        if tab[i] == cible:
            return i
    return -1