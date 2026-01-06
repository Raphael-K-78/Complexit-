def tri_rapide(tab):
    if len(tab) <= 1:
        return tab
    pivot = tab[0]
    gauche = [x for x in tab[1:] if x <= pivot]
    droite = [x for x in tab[1:] if x > pivot]
    return tri_rapide(gauche) + [pivot] + tri_rapide(droite)