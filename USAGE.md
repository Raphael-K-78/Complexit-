# Utilisation des Benchmarks

Ce projet contient **deux benchmarks** permettant de comparer les performances de différents algorithmes .

- Benchmark Tri
- Benchmark Recherche

## Benchmark Tri
Ce benchmark permet de tester les algorithmes de tri en **choisissant les paramètres au moment de l’exécution**.

```bash
python Benchmark_tri.py
```
### **Étape 1 : Choix des tailles**:

Le programme demande d’entrer les tailles des listes à tester.
```bash
Taille de la liste : 100
Taille de la liste : 500
Taille de la liste : 1000
Taille de la liste :
```
Appuyer sur Entréesans rien écrire pour terminer la saisie

### **Étape 2 : Fichier Excel**:

Le programme demande le nom du fichier Excel de sortie
- Par défaut : `resultats.xlsx
- Écraser le fichier répondre O/Y (oui) ou N (non)
- le fichier contient les temps d'éxécution pour chaque algorithme

### **Étape 3 : Diagramme**

Choix du nom du fichier image pour le graphique
- Formats supportés : `.png`, `.jpg`, `.jpeg`
- Par défaut : `graphique.png`

### **Étape 4 : Choix des algorithmes**:

Pour chaque algorithme, répondre O/Y (oui) ou N (non) :
- Tri à bulle
- Tri rapide
- Tri par fusion
- Tri par insertion
- Tri par casier

Seuls les algorithmes sélectionnés seront exécutés et affichés.

### **Résultat**
- Affichage des temps dans le terminal
- Sauvegarde des résultats dans un fichier Excel
- Génération d'un diagramme comparatif

## Benchmark Recherche
Ce benchmark permet de tester les algorithmes de recherche en **choisissant les paramètres au moment de l’exécution**.

```bash
python Benchmark_recherche.py
```
### **Étape 1 : Choix des tailles**:

Le programme demande d’entrer les tailles des listes à tester.
```bash
Taille de la liste : 100
Taille de la liste : 500
Taille de la liste : 1000
Taille de la liste :
```
Appuyer sur Entréesans rien écrire pour terminer la saisie

### **Étape 2 : Fichier Excel**:

Le programme demande le nom du fichier Excel de sortie
- Par défaut : `resultats.xlsx
- Écraser le fichier répondre O/Y (oui) ou N (non)
- le fichier contient les temps d'éxécution pour chaque algorithme

### **Étape 3 : Diagramme**

Choix du nom du fichier image pour le graphique
- Formats supportés : `.png`, `.jpg`, `.jpeg`
- Par défaut : `graphique.png`

### **Résultat**
- Affichage des temps dans le terminal
- Sauvegarde des résultats dans un fichier Excel
- Génération d'un diagramme comparatif
