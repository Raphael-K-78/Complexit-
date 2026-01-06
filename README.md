# Complexité - Raphaël Kondratiuk : MMi3-FA-DW
## Introduction
La complexité d'un Algorithme mesure les valeurs de temps d'éxécution et de mémoire nécéssaire selon la taille des données d'entrée (N). L'objectif est d'évaluer le nombre d'opération en fonction de N. L'objectif est de comparer divers algorithmes afin de déterminer le plus éfficace pour résoudre un problème donnée.
 
La comparaison est faites par 2 valeurs:

- **Temps d'exécution**: Combien d'opérations sont effectuées selon N.

- **Mémoire Utilisée**: Combien d'espace est requis pour stocker l'ensemble des données et variables.

## La notation grand O
La notation grand O permet de donnée une information approximative du nombre d'opération effectuées dans la pire des situations.

Principales Classes de complexité:


| **Classe** | **Nom Courant**| **Comportement si on douple N** |
| --- | --- | --- |
| O(1) | Constant | Même Temps |
| O(log N) | Logarithmique | Un peu plus long |
| O(N) | Linéaire | 2x plus long |
| O(N log N) | Linéarithmique | 2x + un peu plus long |
| O(N²) | Quadratique | 4x plus long |
| O(N³) | Cubique | 8x plus long |
| O(2^N) | Exponentiel | Très long, croissance rapide |

## Partie 1 - Complexité des Algorithmes
### 1.1 - Recherche du Maximum dans un tableau
L'objectif est de trouver le plus grand élément d'un tableau de n éléments

**Algorithme en Python**:
```py
def trouver_maximum(tableau):
    max_val = tableau[0]
    for i in range(1, len(tableau)):
        if tableau[i] > max_val:
            max_val = tableau[i]
    return max_val
```

**Analyse du code**:
1. Taille des donées : n = taille du tableau
2. Boucle qui parcourt tous les données 1x
3. Chaque boucle on compare à la valeur du tableau

**Complexité**:

La complexité de chaque comparaison correspond à O(1)
O(n) La complexité de l'algorithme est linéaire
Dans le cas ou le maximum se trouve au début on considère le cas le moins aventageux ou le maximum est à la fin.

### 1.2 - Algorithmes factorielle itéractive
L'objectif est de calculer le produit de tous les entiers positif de 1 jusqu'à n noter n! qui se lit factorielle de n.

**Algorithme en Python**:
```py
def factorielle_iterative(n):
    resultat = 1
    for i in range(2, n + 1):
        resultat *= i
    return resultat
```

**Analyse du code**:
1. Taille des données : n
2. La boucle effectue n - 1 multiplications

**Complexité**:

Chaque multiplications ont une complexité de O(1)
la complexité est linéaire O(n)

### 1.3 - Algorithme factorielle récursive
L'objectif est le même que précédemment mais en utilisant la récursion.

**Algorithme en Python**:
```py
def factorielle_recursive(n):
    if n <= 1:
        return 1
    return n * factorielle_recursive(n - 1)
```
**Analyse du code**:
1. Taille des données: n
2. Chaque appel de la fonction multiplie n par la factorielle de n - 1
3. Nombre total d'appels récursifs = n

**Complexité**:

Chaque appel correspond à O(1) et il y a (n) appelle
La complexité est de O(n)
La version récurcive utilise plus de mémoire à cause de la pile d'appels.

### 1.4 - Suite de Fibonacci itérative
L'objectif est de calculer le n-ième terme de la suite de Fibonacci 

**Algorithme en Python**:
```py
def fibonacci_iterative(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b
```
**Analyse du code**:
1. Taille des données: n -> rang du terme 
2. Boucle qui parcourt tous les indices de 2 à n
3. Chaque itération effectue une addition

**Complexité**:

Chaque itération correspond à O(1) et il y a (n) appelle
La complexité est de O(n)

### 1.5 - Suite de Fibonacci récurcive
L'objectif est le même mais avec un algorithme récurcive

**Algorithme en Python**:
```py
def fibonacci_recursive(n):
    if n <= 1:
        return n
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)
```
**Analyse du code**:
1. Taille des données: n -> rang du terme 
2. Chaque appel génère 2 appels récurcifs
3. le nombre total d'appels augmente de 2 à la puissance n

**Complexité**:

La complexité est exponentielle soit O(2^n), cette version devient lent pour n>30. La version itérative du programme est beaucoup plus éfficace

### 1.6 - Somme des paires dans un tableau
L'objectif est de calculer toutes les paires distinctes dans un tableau de taille n.

**Algorithme en Python**:
```py
def somme_des_paires(tableau):
    somme = 0
    n = len(tableau)
    for i in range(n):
        for j in range(i + 1, n):
            somme += tableau[i] + tableau[j]
    return somme
```

**Analyse du code**:
1. Taille des données: n -> longueur du tableau
2. Boucle 1: n itérations
3. Boucle 2: n-1, n-2 -> n(n-1)/2
4. addition

**Complexité**:

Chaque addition contient O(1) 
Le nombre total d’opérations est proportionnel à n²
O(n²)

## Partie 2 - Diviser pour régner: Le Théorème Maîtr.
La stratégie diviser pour régner consiste à découper un problème en plusieurs sous-problèmes plus petits, à les résoudre récursivement, puis à combiner leurs résultats. Cette approche permet souvent de réduire fortement le temps d’exécution.

### 2.1 - Recherche naïve dans un tableau trié
L'objectif est de rechercher un entier dans un tableau trié en parcourant les élément un par un 
**Algorithme en Python**:
```py
def recherche_naive(tab, cible):
    for i in range(len(tab)):
        if tab[i] == cible:
            return i
    return -1
```
**Analyse du code**:
1. Taille des données: n -> longeur du tableau
2. Une seul boucle parcourant le tableau
3. Une comparaison à chaque itération

**Complexité**:

Dans la pire des situations l'élément recherché est à la fin du tableau ou absent la complexité est donc de O(n)

### 2.2 - Recherche dichotomique dans un tableau trié
L'objectif est de faire en sorte de réduire le nombre de comparaison grâce au faite que le tableau est trié

** Algorithme en python**:
```py
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
```

**Analyse du code**:
1. Taille des données: n -> longeur du tableau
2. A chaque itération, la taille du tableau divisée par 2
3. si le chiffre du milieu est égal à la cible alors on retourne la valeur si elle est inferieur à la cible alors on ajoute 1 sinon on retire 1. Si la cible n'est pas dans le tableau on retourne -1

**Complexité**:

Relation de récurrence:
T(n) = T(n/2) + O(1)

Application du théorème maître:
- a = 1
- b = 2
- d = 0

log<min>2</min>(1) = 0 => d = log<min>b</min>(a)

Complexité
O(log n)

### 2.3 - Comparatif des temps d’exécution
L’objectif est de comparer la recherche naïve et la recherche dichotomique sur différentes tailles de données.

**Algorithme en python**:
l'ensemble de l'algorithme à sont dans les fichiers lister ci dessous
- recherche/Recherche_dichotomique.py
- recherche/Recherche_naive.py
- save_excel.py
- Benchmark_recherche.py

**Analyse du code**:
1. Génération d’une liste triée de taille taille avec des valeurs aléatoires.
2. Choix aléatoire d’une cible dans la liste.
3. Mesure du temps d’exécution de la recherche naïve.
4. Mesure du temps d’exécution de la recherche dichotomique.
5. Stockage des tailles et temps dans un dictionnaire resultats.
6. Transformation du dictionnaire en DataFrame et sauvegarde dans un fichier Excel.
7. Création du graphique avec deux courbes (naïve et dichotomique).
8. Sauvegarde du graphique dans un fichier.
9. Affichage du graphique à l’écran (si possible).

**Conclusion**:
> d'après les chiffres qu'a pu générer le benchmark on peut conclure que la recherche par dichotomie est optimisé que la recherche naïve

### 2.4 - Multiplication de matrices avec un algorithme naif
Multiplier deux matrices X et Y de taille n×n en utilisant l’algorithme classique, avec trois boucles imbriquées.

**Algorithme en python**:
```py
def multiplication_naive(X, Y):
    n = len(X)
    Z = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                Z[i][j] += X[i][k] * Y[k][j]
    return Z
```

**Analyse du code**:
1. Taille des données : n → dimension des matrices
2. Boucle externe: calcule chaque ligne de la matrice résultat.
3. Boucle intermédiaire: calcule chaque élément de la ligne i.
4. Boucle interne: effectue la somme des produits pour l’élément Z[i][j].

**Complexité**:

chaque boucle fait n itérations
Total d’opérations : 
n×n×n=n^3
Donc complexité temporelle : O(n³)
Mémoire : O(n²) pour la matrice résultat

### 2.5 - Diviser pour conquérir
**Décomposition du problème** :

On a deux matrices X et Y de taille n x n :

X = [ A  B <br>
      C  D ]

Y = [ E  F <br>
      G  H ]

Alors :
XY = [ AE + BG   AF + BH <br> CE + DG   CF + DH ]

- On divise chaque matrice en 4 sous-matrices de taille n/2 x n/2.
- Chaque multiplication devient 8 multiplications de sous-matrices de taille n/2.
- Les additions des produits donnent les éléments de la matrice résultat.

**Paramètres du théorème maître**:

La récurrence du temps est :
T(n) = a * T(n/b) + O(n^d)
- a = 8 → 8 sous-problèmes (multiplications de matrices n/2 x n/2)
- b = 2 → taille des sous-problèmes divisée par 2
- d = 2 → coût des additions de matrices de taille n/2

**Complexité via le théorème maître**:

- Calcul : log2(a) = log2(8) = 3
- Comparaison avec d = 2 → d < log2(a) → cas 1 du théorème maître
- Complexité finale :

T(n) = O(n^3)

> Même complexité que l’algorithme naïf, mais avec une approche récursive “diviser pour conquérir”.


**Résumé des paramètres**:
| **Paramètre** | **Valeur** | **Explication** |
| -- | -- | -- |
| a | 8 | Nombre de sous-problèmes (multiplications) |
| b | 2	| Taille des sous-matrices divisée par 2 |
| d | 2	| Coût des additions de matrices de taille n/2 |
| Complexité finale | O(n³) | Même ordre que l’algorithme naïf | 

### 2.6 - Multiplication de matrices optimisée
On peut améliorer l’approche « diviser pour conquérir » précédente en réduisant le nombre de multiplications récursives.

Au lieu d’effectuer 8 multiplications de matrices de taille n/2 × n/2, l’algorithme de Strassen permet de n’en faire que 7, au prix de quelques additions et soustractions supplémentaires.

**Principe**

On considère toujours les matrices découpées en blocs :

X = [ A  B  
      C  D ]

Y = [ E  F  
      G  H ]

On calcule les 7 produits intermédiaires :

M1 = (A + D)(E + H)  
M2 = (C + D)E  
M3 = A(F − H)  
M4 = D(G − E)  
M5 = (A + B)H  
M6 = (C − A)(E + F)  
M7 = (B − D)(G + H)

À partir de ces produits, on reconstitue la matrice résultat à l’aide d’additions et de soustractions de matrices.

**Paramètres du théorème maître**

La récurrence du temps devient :
T(n) = a * T(n/b) + O(n^d)

- a = 7 → 7 sous-problèmes (multiplications de matrices n/2 × n/2)
- b = 2 → taille des sous-problèmes divisée par 2
- d = 2 → coût des additions/soustractions de matrices de taille n/2

**Complexité via le théorème maître**

- Calcul : log2(a) = log2(7) ≈ 2,81
- Comparaison avec d = 2 → d < log2(a) → cas 1 du théorème maître
- Complexité finale :

T(n) = O(n^{log2(7)}) ≈ O(n^{2,81})

**Résumé des paramètres**

| **Paramètre** | **Valeur** | **Explication** |
| -- | -- | -- |
| a | 7 | Nombre de sous-problèmes (multiplications) |
| b | 2 | Taille des sous-matrices divisée par 2 |
| d | 2 | Coût des additions de matrices de taille n/2 |
| Complexité finale | O(n^{2,81}) | Meilleure que l’algorithme naïf |

> Cette approche est asymptotiquement plus efficace que l’algorithme naïf, mais elle est plus complexe à implémenter et n’est pas toujours plus rapide pour de petites tailles de matrices.

## Partie 3 - Tris
### 3.1 - Tri à Bulle (Bubble Sort)
L'objectif est de Parcourir un tableau et d'échanger les éléments consécutifs si nécessaire, jusqu’à ce que le tableau soit trié.

**Algorithme en python**:
```py
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
```

**Analyse du code**:
1. Taille des données : n → nombre d’éléments du tableau
2. Boucle externe : continue tant qu’il y a eu une permutation lors du passage précédent
3. Boucle interne : compare chaque élément avec son suivant et échange si nécessaire

**Complexité**
- Boucle interne : n itérations
- Boucle externe : jusqu’à n passages
- Total d’opérations : O(n²)
- Mémoire : O(1) supplémentaire (tri sur place)

### 3.2 - Tri par Insertion (Insertion Sort)
L'objectif est de Prendre les éléments un par un et les insérer à la bonne position parmi ceux déjà triés.

**Algorithme en python**:
```py
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
```

**Analyse du code**:
1. Taille des données : n → nombre d’éléments du tableau
2. Boucle externe : parcourt chaque élément à insérer
3.Boucle interne : décale les éléments plus grands pour insérer la valeur

**Complexité**:

- Meilleur cas : O(n) (tableau déjà trié)
- Cas moyen et pire cas : O(n²)
- Mémoire : O(1) supplémentaire

### 3.3 - Tri Fusion (Merge Sort)
L'objectif est de diviser récursivement le tableau en deux, trier chaque moitié, puis fusionne.

**Algorithme en python**:
```py
def tri_fusion(tab):
    if len(tab) <= 1:
        return tab
    mid = len(tab) // 2
    left = tri_fusion(tab[:mid])
    right = tri_fusion(tab[mid:])
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result
```

**Analyse du code**:
1. Taille des données : n → nombre d’éléments du tableau
2. Division récursive : le tableau est découpé en deux jusqu’à ce que chaque sous-tableau ait 1 élément
3. Fusion : reconstitue le tableau trié à partir des deux sous-tableaux

**Complexité**
- Nombre de divisions : log₂(n)
- Fusion : O(n) à chaque niveau
- Complexité totale : O(n log n)
- Mémoire : O(n) pour les tableaux temporaires

### 3.4 - Tri Rapide (Quick Sort)
L'objectif est de Partitionner le tableau autour d’un pivot et de trier récursivement les deux sous-parties.

**Algorithme en python**:
```py
def tri_rapide(tab):
    if len(tab) <= 1:
        return tab
    pivot = tab[0]
    gauche = [x for x in tab[1:] if x <= pivot]
    droite = [x for x in tab[1:] if x > pivot]
    return tri_rapide(gauche) + [pivot] + tri_rapide(droite)
```

**Analyse du code**:
1. Taille des données : n → nombre d’éléments du tableau
2. Partition : sépare les éléments plus petits ou plus grands que le pivot
3. Récursion : trie les sous-tableaux gauche et droite

**Complexité**

- Meilleur cas : O(n log n)
- Pire cas (tableau déjà trié et pivot mal choisi) : O(n²)
- Mémoire : O(n) pour les sous-tableaux

### 3.5 - Tri Casier (Counting Sort)
L'objectif est de Compter le nombre d’occurrences de chaque valeur puis reconstituer le tableau trié.

**Algorithme en python**:
```py
def tri_casier(tab):
    a, b = min(tab), max(tab)
    T = [0] * (b - a + 1)
    for x in tab:
        T[x - a] += 1
    result = []
    for i, count in enumerate(T):
        result.extend([i + a] * count)
    return result
```

**Analyse du code**:
1. Taille des données : n → nombre d’éléments du tableau, b − a → intervalle des valeurs
2. Comptage : calcule combien de fois chaque valeur apparaît
3. Reconstruction : génère le tableau trié à partir du tableau de comptage

**Complexité**
- O(n + k) Pas de meilleur/pire cas compliqué : toujours linéaire par rapport à n et k.
- Mémoire : O(k + n) k pour le tableau de comptage, n pour le tableau trié final.

### 3.6 - Comparatif des temps d’exécution
L’objectif est de comparer les différentes fonctions de tri sur différentes tailles de données.

**Algorithme en python**:

l'ensemble de l'algorithme à sont dans les fichiers lister ci dessous
- tri/tri_bulle.py
- tri/tri_casier.py
- tri/tri_fusion.py
- tri/tri_insertion.py
- tri/tri_rapide.py
- save_excel.py
- Benchmark_tri.py
- fmt_time.py

**Analyse du code**:
1. Génération d’une liste  de taille taille avec des valeurs aléatoires.
2. Mesure du temps d’exécution du tri à bulle.
3. Mesure du temps d’exécution du tri casier.
4. Mesure du temps d’exécution du tri fusion.
5. Mesure du temps d’exécution du tri par insertion.
6. Mesure du temps d’exécution du tri rapide.
7. Stockage des tailles et temps dans un dictionnaire resultats.
8. Transformation du dictionnaire en DataFrame et sauvegarde dans un fichier Excel.
9. Création du graphique avec deux courbes (naïve et dichotomique).
10. Sauvegarde du graphique dans un fichier.
11. Affichage du graphique à l’écran (si possible).

**Conclusion**:
> d'après les chiffres qu'a pu générer le benchmark on peut conclure que le tri casier est le plus optimisé alors que le tri à bulle est le moins optimisé avec le tri par insertion
