def recherche_dichotomique(tab, cible):
    gauche = 0
    droite = len(tab) - 1

    while gauche <= droite:
        milieu = (gauche + droite) // 2

        if tab[milieu] == cible:
            return milieu
        elif tab[milieu] < cible:
            gauche = milieu + 1
        else:
            droite = milieu - 1

    return -1